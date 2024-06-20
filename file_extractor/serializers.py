from rest_framework import serializers
from .models import UploadedFile, ProcessedData


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = '__all__'

class ProcessedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedData
        fields = ('name', 'value', 'sheet_name', 'row_number', 'column_number')
