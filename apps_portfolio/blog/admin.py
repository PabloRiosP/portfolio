from django.contrib import admin

from .models import Blog

@admin.register(Blog)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
