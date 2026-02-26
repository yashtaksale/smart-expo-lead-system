from django.db.models import Count
from visitors.models import Visitor


def get_dashboard_analytics():


    total_visitors = Visitor.objects.count()

    category_distribution = (
        Visitor.objects
        .values("category")
        .annotate(count=Count("id"))
    )

    lead_distribution = (
        Visitor.objects
        .values("lead_score")
        .annotate(count=Count("id"))
    )

    whatsapp_status_distribution = (
        Visitor.objects
        .values("whatsapp_status")
        .annotate(count=Count("id"))
    )

    hot_leads = Visitor.objects.filter(lead_score="hot").count()

    today_visitors = Visitor.objects.filter(
        created_at__date__gte=Visitor.objects.latest("created_at").created_at.date()
    ).count() if total_visitors > 0 else 0

    return {
        "total_visitors": total_visitors,
        "category_distribution": list(category_distribution),
        "lead_distribution": list(lead_distribution),
        "whatsapp_status_distribution": list(whatsapp_status_distribution),
        "hot_leads": hot_leads,
        "today_visitors": today_visitors,
    }
