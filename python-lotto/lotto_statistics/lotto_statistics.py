from enum import Enum, unique


@unique
class LottoStatisticMatchingNumber(Enum):
    THREE_MATCHED = (4, 3, 5000)
    FOUR_MATCHED = (3, 4, 20000)
    FIVE_MATCHED = (2, 5, 100000)
    SIX_MATCHED = (1, 6, 5000000)

    def __init__(self, rank, matched_count, price):
        self.rank = rank
        self.matched_count = matched_count
        self.price = price


def get_winning_lotto_result(automatic_random_lotteries: list, last_week_winning_lotto: list) -> dict:
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
        lotto_matching_statistic[lotto_matched_index.matched_count] = \
            winning_matched_count_numbers.count(lotto_matched_index.matched_count)
    return lotto_matching_statistic
