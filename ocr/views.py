from django.http import JsonResponse
from . import ocr_module, spell_checker
from urllib import parse


def ocr_image(request):
    ocr_result = ocr_module.ocr(request.GET['path'])

    correct_text = request.GET['correctText']

    if correct_text is None:
        spell_check_result = spell_checker.check(' '.join(ocr_result))
    else:
        correct_text = parse.unquote(correct_text)
        spell_check_result = spell_checker.check_with_correct(' '.join(ocr_result), correct_text)

    return JsonResponse(spell_check_result)
