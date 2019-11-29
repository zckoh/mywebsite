from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','technology','created_at')
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(Project, ProjectAdmin)
