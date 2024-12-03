from django.contrib import admin
from .models import TodoItem

@admin.register(TodoItem)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'due_date', 'status']
    search_fields = ['title', 'description', 'tags']
    list_filter = ['status', 'due_date']
