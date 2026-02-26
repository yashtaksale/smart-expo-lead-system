from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.conf import settings
import openpyxl
import qrcode
from io import BytesIO

from .whatsappsender import send_whatsapp_message
from .forms import VisitorForm
from .models import WhatsAppLog, Visitor
from visitors.visitors.services.lead_scoring_service import calculate_lead_score


def entry_mode(request):
    total_count = Visitor.objects.count()
    return render(request, "visitors/entry_mode.html", {
        "total_count": total_count
    })

def admin_required(request):
    if request.session.get("admin_authenticated") != True:
        return False
    return True

def signup(request):
    total_count = Visitor.objects.count()

    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data.get("phone")

            if phone and Visitor.objects.filter(phone=phone).exists():
                form.add_error("phone", "This number is already registered.")
                return render(request, "visitors/signup.html", {
                    "form": form,
                    "total_count": total_count,
                })

            visitor = form.save(commit=False)
            visitor.lead_score = calculate_lead_score(visitor)
            visitor.save()

            WhatsAppLog.objects.create(
                visitor=visitor,
                status="pending",
                attempts=0
            )

            request.session["group_members"] = None
            request.session["current_group"] = None

            return redirect("thanks")
    else:
        form = VisitorForm()

    return render(request, "visitors/signup.html", {
        "form": form,
        "total_count": total_count,
    })


def group_signup(request):
    if request.method == "POST":
        group_name = request.POST.get("group_name")
        request.session["group_name"] = group_name
        request.session["current_group"] = group_name
        request.session["group_members"] = []
        return redirect("group-add")

    return render(request, "visitors/group_signup.html")


def group_add_member(request):
    group_name = request.session.get("group_name")

    if not group_name:
        return redirect("group-signup")

    members = request.session.get("group_members", [])

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        company = request.POST.get("company")
        email = request.POST.get("email")
        message = request.POST.get("message")
        category = request.POST.get("category")

        if name:
            if phone and Visitor.objects.filter(phone=phone).exists():
                return redirect("group-add")

            visitor = Visitor.objects.create(
                name=name,
                phone=phone,
                company=company,
                email=email,
                message=message,
                category=category,
                group_label=group_name
            )

            visitor.lead_score = calculate_lead_score(visitor)
            visitor.save()

            WhatsAppLog.objects.create(
                visitor=visitor,
                status="pending",
                attempts=0
            )

            members.append({
                "name": name,
                "phone": phone,
                "company": company,
                "email": email,
                "message": message,
                "category": category,
                "lead_score": visitor.lead_score
            })

            request.session["group_members"] = members
            request.session.modified = True

        return redirect("group-add")

    return render(request, "visitors/group_add_member.html", {
        "group_name": group_name,
        "members": members
    })


def camera_capture(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == "POST" and request.FILES.get("photo"):
        visitor.photo = request.FILES["photo"]
        visitor.save()

        if visitor.phone:
            try:
                send_whatsapp_message(visitor.phone, visitor.name)

                visitor.whatsapp_status = "Sent"
                visitor.whatsapp_retry_count += 1
                visitor.save()

                WhatsAppLog.objects.filter(visitor=visitor).update(
                    status="sent",
                    attempts=1,
                    sent_at=timezone.now()
                )

            except Exception:
                visitor.whatsapp_status = "Failed"
                visitor.save()

                WhatsAppLog.objects.filter(visitor=visitor).update(
                    status="failed",
                    attempts=1
                )

        return redirect("thanks")

    return render(request, "visitors/camera.html", {
        "visitor": visitor
    })


def thanks(request):
    visitor = Visitor.objects.order_by("-id").first()
    group_members = request.session.get("group_members")
    group_name = request.session.get("current_group")

    return render(request, "visitors/thanks.html", {
        "visitor": visitor,
        "group_members": group_members,
        "group_name": group_name,
    })

def latest_visitor_json(request):
    group = request.session.get("group_members")
    group_name = request.session.get("current_group")

    if group:
        return JsonResponse({
            "ok": True,
            "mode": "group",
            "group_name": group_name,
            "members": group
        })

    visitor = Visitor.objects.order_by("-created_at").first()

    if visitor:
        return JsonResponse({
            "ok": True,
            "mode": "single",
            "name": visitor.name,
            "company": visitor.company,
        })

    return JsonResponse({"ok": False})


def tv_display(request):
    return render(request, "visitors/tv.html")


def admin_tools(request):
    if request.session.get("admin_authenticated") != True:
        return redirect("admin-login")

    return render(request, "visitors/admin_tools.html", {
        "total": Visitor.objects.count(),
        "hot": Visitor.objects.filter(lead_score="hot").count(),
        "warm": Visitor.objects.filter(lead_score="warm").count(),
        "cold": Visitor.objects.filter(lead_score="cold").count(),
        "sent": Visitor.objects.filter(whatsapp_status="Sent").count(),
        "pending": Visitor.objects.filter(whatsapp_status="Pending").count(),
        "failed": Visitor.objects.filter(whatsapp_status="Failed").count(),
        "students": Visitor.objects.filter(category="student").count(),
        "business": Visitor.objects.filter(category="business").count(),
        "investors": Visitor.objects.filter(category="investor").count(),
        "vendors": Visitor.objects.filter(category="vendor").count(),
        "jobs": Visitor.objects.filter(category="job").count(),
    })

def export_visitors_excel(request):
    if not admin_required(request):
        return redirect("admin-login")

    import openpyxl
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Visitors"

    ws.append([
        "ID", "Name", "Phone", "Company",
        "Email", "Category", "Lead Score",
        "WhatsApp Status", "Group", "Created At"
    ])

    for v in Visitor.objects.all():
        ws.append([
            v.id, v.name, v.phone, v.company,
            v.email, v.category, v.lead_score,
            v.whatsapp_status, v.group_label,
            v.created_at.strftime("%Y-%m-%d %H:%M:%S")
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="visitors.xlsx"'
    wb.save(response)
    return response

def reset_counter(request):
    if not admin_required(request):
        return redirect("admin-login")

    Visitor.objects.all().delete()
    WhatsAppLog.objects.all().delete()
    request.session.flush()
    return redirect("entry-mode")

def delete_last_visitor(request):
    if not admin_required(request):
        return redirect("admin-login")

    last_visitor = Visitor.objects.order_by("-created_at").first()
    if last_visitor:
        last_visitor.delete()
    return redirect("entry-mode")

def qr_entry(request):
    host = request.get_host()
    url = f"http://{host}/signup/"

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")


def generate_qr(request, visitor_id):
    url = f"http://192.168.1.6:8000/camera/{visitor_id}/"

    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    return HttpResponse(buffer.getvalue(), content_type="image/png")



def admin_login(request):
    if request.method == "POST":
        password = request.POST.get("password")

        if password == settings.ADMIN_ACCESS_PASSWORD:
            request.session["admin_authenticated"] = True
            return redirect("admin-tools")
        else:
            return render(request, "visitors/admin_login.html", {
                "error": "Wrong Password ❌"
            })

    return render(request, "visitors/admin_login.html")