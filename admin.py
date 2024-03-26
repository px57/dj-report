from django.contrib import admin
from report import models

class ReportTemplateTranslationInline(admin.TabularInline):
    """
        @description: ReportTemplateTranslationInline
    """

    model = models.ReportTemplateTranslation
    extra = 0

    fields = [
        'language',
        'title',
        'description',
    ]
    formfield_overrides = {

    }

@admin.register(models.ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    """
    The report template admin.
    """
    list_display = ('title', 'interface')
    search_fields = ('title',)
    inlines = [ReportTemplateTranslationInline]

@admin.register(models.Reported)
class ReportedAdmin(admin.ModelAdmin):
    """
    The reported admin.
    """
    list_display = ('profile', 'template')
    search_fields = ('profile', 'template')