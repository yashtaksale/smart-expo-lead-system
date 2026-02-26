import time
from django.utils import timezone
from .models import WhatsAppLog
from .whatsappsender import send_whatsapp_message

def process_queue():
    while True:
        pending = WhatsAppLog.objects.filter(status="pending")

        for log in pending:
            try:
                send_whatsapp_message(log.visitor.phone, log.visitor.name)
                log.status = "sent"
                log.sent_at = timezone.now()
            except:
                log.attempts += 1
                log.status = "failed"

            log.save()

        time.sleep(30)
