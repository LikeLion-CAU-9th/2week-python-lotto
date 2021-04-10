import random

LOTTO_FIRST_NUMBER = 1
LOTTO_LAST_NUMBER = 46
LOTTO_LENGTH = 6


def lotto_number_generator():
    lotto_numbers = random.sample(range(LOTTO_FIRST_NUMBER, LOTTO_LAST_NUMBER), LOTTO_LENGTH)
    lotto_numbers.sort()
    return lotto_numbers
