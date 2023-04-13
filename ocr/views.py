from django.http import JsonResponse
from . import ocr_module, spell_checker


def ocr_image(request):
    ocr_result = ocr_module.ocr(request.GET['path'])

    spell_check_result = spell_checker.check(''.join(ocr_result))

    return JsonResponse(spell_check_result)
