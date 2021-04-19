from lotto_ticket.lotto_information import LottoInformation
from ui.inputer import input_purchased_lotto_total_amount, input_last_week_winning_lotto
from lotto_ticket.lotto_generator import lotto_number_generator


def get_automatic_random_lotteries():
    random_lotteries = []
    purchased_lotto_total_amount = input_purchased_lotto_total_amount()
    number_of_lotto = calculate_number_of_lotto(purchased_lotto_total_amount)

    for lotto_count in range(number_of_lotto):
        random_lotteries.append(lotto_number_generator())

    return random_lotteries, purchased_lotto_total_amount


def calculate_number_of_lotto(purchased_lotto_amount: int):
    return purchased_lotto_amount // LottoInformation.LOTTO_PRICE


def get_last_week_winning_lotto():
    last_week_winning_lotto = input_last_week_winning_lotto()
    return last_week_winning_lotto
