from django.db import models


class Visitor(models.Model):
    CATEGORY_CHOICES = [
        ("student", "Student"),
        ("business", "Business Owner"),
        ("investor", "Investor"),
        ("vendor", "Vendor"),
        ("job", "Job Seeker"),
    ]

    LEAD_SCORE_CHOICES = [
        ("hot", "Hot 🔥"),
        ("warm", "Warm"),
        ("cold", "Cold"),
    ]

    WHATSAPP_STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Sent", "Sent"),
        ("Failed", "Failed"),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    company = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    message = models.TextField(blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="student"
    )

    lead_score = models.CharField(
        max_length=10,
        choices=LEAD_SCORE_CHOICES,
        default="warm"
    )

    whatsapp_status = models.CharField(
        max_length=20,
        choices=WHATSAPP_STATUS_CHOICES,
        default="Pending"
    )

    whatsapp_retry_count = models.IntegerField(default=0)

    photo = models.ImageField(
        upload_to="visitor_photos/",
        blank=True,
        null=True
    )

    group_label = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"


class WhatsAppLog(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="pending")
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.visitor.name} - {self.status}"