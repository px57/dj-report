from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from report.rules.stack import REPORT_RULESTACK


class ReportTemplateTranslation(BaseMetadataModel):
    """
    The report template translation model.
    """
    language = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

class ReportTemplate(BaseMetadataModel):
    """
    The report model.
    """
    interface = models.CharField(
        max_length=100,
        choices=REPORT_RULESTACK.models_choices(),
        default='default'
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(
        upload_to='reports/',
        null=True,  
        blank=True
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

class Reported(BaseMetadataModel):
    """
    The reported class.
    """

    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    template = models.ForeignKey(
        ReportTemplate,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
