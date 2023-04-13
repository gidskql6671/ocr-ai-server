from hanspell import spell_checker


def check(input_str):
    spell_check_result = spell_checker.check(input_str)

    checked_count = len(spell_check_result.words.items())

    error_count = spell_check_result.errors

    print(spell_check_result.checked)
    print(error_count)

    return {
        "answer_percent": (checked_count - error_count) / checked_count,
        "correct_string": spell_check_result.checked,
        "origin_string": input_str
    }
