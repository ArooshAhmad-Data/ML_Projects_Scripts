import base64

import cv2
import numpy as np
from django.shortcuts import render
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .image_processing import process_image
from .serializers import ImageSerializer


def image_upload_view(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        processed_image = process_image(image_file)

        # Save the processed image to a temporary file
        temp_file = InMemoryUploadedFile(
            processed_image,
            None,  # field_name
            'processed.jpg',  # file_name
            'image/jpeg',  # content_type
            processed_image.tell,  # size
            None  # charset
        )

        context = {'processed_image': temp_file}
    else:
        context = {}

    return render(request, 'image_upload.html', context)

def process_uploaded_image(image):

    image = process_image(image)

    return image

class ImageProcessAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            processed_image_base64 = process_uploaded_image(serializer.validated_data['image'])
            # return Response({"image":processed_image_base64})
            return Response(processed_image_base64)
        else:
            return Response(serializer.errors, status=400)