from django.db import models
from django.core.validators import FileExtensionValidator


class UploadedFile(models.Model):
    file = models.FileField( 
        validators=[FileExtensionValidator(allowed_extensions=['xls', 'xlsx'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} uploaded at {self.uploaded_at}"


class ProcessedData(models.Model):
    uploaded_file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE, related_name='processed_data')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length= 255, null=True, blank=True)
    sheet_name = models.CharField(max_length=100, null=True, blank=True)
    row_number = models.PositiveIntegerField(null=True, blank=True)
    column_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
