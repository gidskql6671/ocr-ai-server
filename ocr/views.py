from django.http import HttpResponse
from . import ocr_module


def ocr_image(request):
    result = ocr_module.ocr(request.GET['path'])

    return HttpResponse(result)
