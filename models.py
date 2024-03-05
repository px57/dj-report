
from django.conf import settings
from django.db import models
from django.forms.models import model_to_dict

from kernel.models.base_metadata_model import BaseMetadataModel
from report.rules.stack import REPORT_RULESTACK
from kernel.models.serialize import serializer__serialize__
from kernel.i18n.models import translateDBQuerySet, translateDBObject
from kernel.models.serialize import serializer__init__

class ReportTemplateTranslation(BaseMetadataModel):
    """
    The report template translation model.
    """
    language = models.CharField(
        'language',
        max_length=255,
        default='fr',
        choices=settings.LANGUAGE_DB_CHOICES,
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    translateObject = models.ForeignKey(
        'report.ReportTemplate',
        on_delete=models.CASCADE,
        related_name='translates',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        """
        Return the language.
        """
        return self.language
    
    @serializer__serialize__
    def serialize(self, request):
        """
        Serialize the report template translation.
        """
        serialize = model_to_dict(self)
        return serialize

class ReportTemplate(BaseMetadataModel):
    """
    The report model.
    """
    translation_model = ReportTemplateTranslation

    @serializer__init__
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    interface = models.CharField(
        max_length=100,
        choices=REPORT_RULESTACK.models_choices(),
        default='default'
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    file = models.FileField(
        upload_to='reports/',
        null=True,  
        blank=True
    )

    order = models.IntegerField(
        default=0
    )

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