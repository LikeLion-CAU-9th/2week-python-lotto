import random

from lotto_ticket.lotto_information import LottoInformation


def lotto_number_generator():
    lotto_numbers = random.sample(
        range(
            LottoInformation.LOTTO_FIRST_NUMBER,
            LottoInformation.LOTTO_LAST_NUMBER
        ), LottoInformation.LOTTO_LENGTH
    )
    lotto_numbers.sort()
    return lotto_numbers
