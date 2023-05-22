from django.http import JsonResponse
from . import ocr_module, spell_checker


def ocr_image(request):
    ocr_result = ocr_module.ocr(request.GET['path'])

    spell_check_result = spell_checker.check(' '.join(ocr_result))

    return JsonResponse(spell_check_result)


def ocr_image_with_correct(request, correct_text):
    ocr_result = ocr_module.ocr(request.GET['path'])

    spell_check_result = spell_checker.check_with_correct(' '.join(ocr_result), correct_text)

    return JsonResponse(spell_check_result)

