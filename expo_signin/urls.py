from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # Django admin panel
    path('', include('visitors.urls')),        # Your visitors app routes
]
