from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'status']
    list_filter = ['date']
    ordering = ['date']
