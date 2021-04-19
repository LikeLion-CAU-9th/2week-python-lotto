def get_winning_lotto_result(automatic_random_lotteries: list, last_week_winning_lotto: list):
    get_winning_matched_number()


def get_winning_matched_number(automatic_random_lotteries: list, last_week_winning_lotto: list):
    winning_lotto_matched_numbers = []
    for automatic_random_lottery in automatic_random_lotteries:
        matched_count = list(set(automatic_random_lottery).intersection(last_week_winning_lotto))
        winning_lotto_matched_numbers.append(matched_count)
    return winning_lotto_matched_numbers
