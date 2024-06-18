from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UploadedFile, ProcessedData
from .serializers import UploadedFileSerializer, ProcessedDataSerializer
from .excel_processor import process_excel_file



class FileUploadViewSet(ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        uploaded_file = serializer.save()
        file_path = uploaded_file.file.path
        processed_data = process_excel_file(file_path)

        if processed_data is not None: 
            processed_data_instances = [
                ProcessedData(
                    uploaded_file=uploaded_file,
                    name=data['name'],
                    value=data['value'],
                    sheet_name=data['sheet_name'],
                    row_number=data['row_number'],
                    column_number=data['column_number']
                )
                for data in processed_data
            ]
            ProcessedData.objects.bulk_create(processed_data_instances)

    def get_serializer_class(self):
        if self.action == 'create':
            return UploadedFileSerializer
        return super().get_serializer_class()
    


class ProcessedDataViewSet(ModelViewSet):
    queryset = ProcessedData.objects.all()
    serializer_class = ProcessedDataSerializer