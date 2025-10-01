from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "priority", "status", "due_date", "created_at")
    list_filter = ("priority", "status", "owner")
    search_fields = ("title", "description")
