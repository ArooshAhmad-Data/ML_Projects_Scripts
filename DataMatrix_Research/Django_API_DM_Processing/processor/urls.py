from django.urls import path
from . import views
from .views import image_upload_view, ImageProcessAPIView

urlpatterns = [
    path('image-upload/', image_upload_view, name='image-upload-view'),
    path('api/image-process/', ImageProcessAPIView.as_view(), name='image-process-api'),
]
