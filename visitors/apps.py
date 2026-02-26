from django.apps import AppConfig


class VisitorsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "visitors"
    verbose_name = "Expo Visitor Management"

    def ready(self):
        """
        App startup hook.
        Keep this clean — do NOT start threads,
        background workers, or Selenium here.
        """
        pass
