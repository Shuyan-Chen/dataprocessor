from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FileUploadViewSet,ProcessedDataViewSet


router = DefaultRouter()
router.register('upload', FileUploadViewSet, basename='upload')
router.register('processed-data', ProcessedDataViewSet, basename='processed-data')

urlpatterns = [

] + router.urls