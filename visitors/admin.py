from django.contrib import admin

from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('name','company','phone','email','created_at')
    list_filter = ('created_at','company')
    search_fields = ('name','company','phone','email')
