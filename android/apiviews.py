import base64
import codecs
import os

from django.contrib.auth import authenticate
from django.core.files import File
from django.db import IntegrityError
from django.db.models import Q
from django.http import JsonResponse
from rest_framework import generics
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Publication
from .serializers import PublicationSerializer


class PublicationApiView(APIView):
    """
        List of all publication, or create a new publication depending on the method of the request.
    """

    def get(self, request, format=None):
        users = Publication.objects.all()
        serializer = PublicationSerializer(users, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PublicationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)