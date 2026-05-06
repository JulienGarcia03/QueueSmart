from django.contrib import admin
from .models import Queue, QueueEntry, Service
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "expected_duration", "priority")
    search_fields = ("name",)
@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ("service", "status", "created_at")
    list_filter = ("status",)

@admin.register(QueueEntry)
class QueueEntryAdmin(admin.ModelAdmin):
    list_display = ("user_name", "queue", "position", "status", "joined_at", "updated_at")
    list_filter = ("status", "queue__service")
    search_fields = ("user_name", "queue__service__name")