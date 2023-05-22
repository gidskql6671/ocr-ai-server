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


def check_with_correct(input_str, correct_str):
    i = 0
    j = 0

    checked_count = 0
    error_count = 0
    while i < len(input_str) and j < len(correct_str):
        if input_str[i] == ' ':
            i += 1
            continue
        if correct_str[j] == ' ':
            j += 1
            continue

        checked_count += 1
        if input_str[i] != correct_str[j]:
            error_count += 1
        i += 1
        j += 1

    while i < len(input_str):
        if input_str[i] == ' ':
            i += 1
            continue
        error_count += 1
        checked_count += 1
        i += 1
    while j < len(correct_str):
        if correct_str[j] == ' ':
            j += 1
            continue
        error_count += 1
        checked_count += 1
        j += 1

    print(checked_count)
    print(error_count)

    return {
        "answer_percent": (checked_count - error_count) / checked_count,
        "correct_string": correct_str,
        "origin_string": input_str
    }
