from django.contrib import admin
from report import models

@admin.register(models.ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    """
    The report template admin.
    """
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(models.Reported)
class ReportedAdmin(admin.ModelAdmin):
    """
    The reported admin.
    """
    list_display = ('profile', 'template')
    search_fields = ('profile', 'template')