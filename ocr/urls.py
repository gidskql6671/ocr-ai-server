from django.urls import path

from . import views

urlpatterns = [
    path("", views.ocr_image, name="ocr"),
]