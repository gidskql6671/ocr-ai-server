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
    input_str_len = len(input_str)
    correct_str_len = len(correct_str)

    if input_str == correct_str:
        answer_percent = 1.
    else:
        lcs_len = get_lcs_len(input_str, correct_str, input_str_len, correct_str_len)

        if lcs_len < correct_str_len:
            answer_percent = lcs_len / correct_str_len
        else:
            answer_percent = correct_str_len / input_str_len

    return {
        "answer_percent": answer_percent,
        "correct_string": correct_str,
        "origin_string": input_str
    }


def get_lcs_len(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]

    i = 0
    prev_i = 1
    for s1_index in range(m + 1):
        for j in range(n + 1):
            if s1_index == 0 or j == 0:
                dp[i][j] = 0
            elif s1[s1_index - 1] == s2[j - 1]:
                dp[i][j] = dp[prev_i][j - 1] + 1
            else:
                dp[i][j] = max(dp[prev_i][j], dp[i][j - 1])
        prev_i = i
        i = (i + 1) % 2

    return dp[prev_i][n]
