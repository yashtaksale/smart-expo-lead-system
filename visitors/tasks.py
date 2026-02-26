from datetime import datetime, timedelta
from django.utils import timezone
from .models import Visitor
from .whatsapp import send_whatsapp_message   # pyright: ignore[reportMissingImports]
from visitors.scheduler import scheduler


def schedule_whatsapp_msg(visitor_id):
    run_time = timezone.now() + timedelta(hours=1)

    scheduler.add_job(
        func=send_message_job,
        trigger='date',
        run_date=run_time,
        args=[visitor_id],
        id=f"message_{visitor_id}",
        replace_existing=True
    )


def send_message_job(visitor_id):
    try:
        visitor = Visitor.objects.get(id=visitor_id)
        send_whatsapp_message(visitor)
        visitor.whatsapp_status = "Sent"
        visitor.save()

    except Exception as e:
        print("Error sending WhatsApp message:", e)
