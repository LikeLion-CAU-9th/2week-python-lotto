from lotto_statistics.lotto_statistics import LottoStatisticMatchingNumber


def get_lotto_profit(winning_lotto_result: dict, purchased_lotto_total_amount: int):
    total_price = get_total_price(winning_lotto_result)
    return float(total_price / purchased_lotto_total_amount)


def get_total_price(winning_lotto_result: dict) -> int:
    total_price = 0
    for lotto_matched_index in LottoStatisticMatchingNumber:
        total_price += winning_lotto_result[lotto_matched_index.matched_count] * lotto_matched_index.price
    return total_price


