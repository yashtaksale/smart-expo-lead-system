from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.entry_mode, name="entry-mode"),

    path("signup/", views.signup, name="signup"),

    path("group/", views.group_signup, name="group-signup"),
    path("group/add/", views.group_add_member, name="group-add"),

    path("thanks/", views.thanks, name="thanks"),
    path("latest/", views.latest_visitor_json, name="latest"),
    path("tv/", views.tv_display, name="tv"),

    path("export/", views.export_visitors_excel, name="export"),

    path("admin-login/", views.admin_login, name="admin-login"),
    path("admin-tools/", views.admin_tools, name="admin-tools"),

    path("reset/", views.reset_counter, name="reset-counter"),
    path("delete-last/", views.delete_last_visitor, name="delete-last"),

    path("camera/<int:visitor_id>/", views.camera_capture, name="camera"),

    path("qr/", views.generate_qr, name="qr"),  
    path("scan/", views.qr_entry, name="qr-entry"), 
    path("generate-qr/<int:visitor_id>/", views.generate_qr, name="generate-qr"),

    path("qr-main-image/", views.qr_entry, name="qr"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
