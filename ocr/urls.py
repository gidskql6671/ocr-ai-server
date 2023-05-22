from django.urls import path

from . import views

urlpatterns = [
    path("", views.ocr_image, name="ocr"),
    path("<str:correct_text>", views.ocr_image_with_correct, name="ocr-with-correct"),
]