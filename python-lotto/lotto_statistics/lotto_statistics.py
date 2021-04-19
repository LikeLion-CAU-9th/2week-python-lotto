from enum import Enum


class LottoStatisticMatchingNumber(Enum):
    THREE_MATCHED = 3
    FOUR_MATCHED = 4
    FIVE_MATCHED = 5
    SIX_MATCHED = 6


def get_winning_lotto_result(automatic_random_lotteries: list, last_week_winning_lotto: list):
    winning_lotto_matched_numbers = get_winning_matched_number(automatic_random_lotteries, last_week_winning_lotto)
    winning_matched_count_numbers = get_winning_matched_count(winning_lotto_matched_numbers)
    return get_lotto_matching_statistic(winning_matched_count_numbers)


def get_winning_matched_number(automatic_random_lotteries: list, last_week_winning_lotto: list):
    winning_lotto_matched_numbers = []
    for automatic_random_lottery in automatic_random_lotteries:
        matched_count = list(set(automatic_random_lottery).intersection(last_week_winning_lotto))
        winning_lotto_matched_numbers.append(matched_count)
    return winning_lotto_matched_numbers


def get_winning_matched_count(winning_lotto_matched_numbers):
    winning_matched_count_numbers = []
    for winning_lotto_matched_number in winning_lotto_matched_numbers:
        winning_matched_count_numbers.append(len(winning_lotto_matched_number))
    return winning_matched_count_numbers


def get_lotto_matching_statistic(winning_matched_count_numbers):
    lotto_matching_statistic = dict()
    for lotto_matched_index in LottoStatisticMatchingNumber:
        lotto_matching_statistic[lotto_matched_index.value] = \
            winning_matched_count_numbers.count(lotto_matched_index.value)
    return lotto_matching_statistic
