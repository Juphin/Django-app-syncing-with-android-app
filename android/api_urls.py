from django.contrib import admin
from django.urls import path

from . import apiviews
from .apiviews import PublicationApiView

urlpatterns = [
    path("pub", PublicationApiView.as_view()),
]
