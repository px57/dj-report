from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel

class Report(BaseMetadataModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='reports/')
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title