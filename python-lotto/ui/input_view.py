# from lotto_ticket.lotto import LottoInformation
from lotto_decorator.printer_decorator import printer_format

INPUT_ZERO_TO_LOTTO_AMOUNT = 0


class InputMessage:
    INPUT_PURCHASED_LOTTO_TOTAL_AMOUNT_MESSAGE = '로또 구입 금액을 입력해주세요: '
    INPUT_INVALID_FORMAT_LOTTO_TOTAL_AMOUNT_MESSAGE = '숫자형식의 금액을 입력해주세요.'
    INPUT_NOT_ZERO_LOTTO_TOTAL_AMOUNT_MESSAGE = '구입할 로또 금액으로 0원을 입력하실 수 없습니다. 로또 한장 이상의 금액을 입력해주세요.'
    INPUT_NOT_SATISFY_MINIMUM_LOTTO_TOTAL_AMOUNT_MESSAGE = "로또 한장 이상의 금액을 입력해주세요."


class NotSatisfyMinimumAmountError(Exception):
    def __init__(self):
        super().__init__(InputMessage.INPUT_NOT_SATISFY_MINIMUM_LOTTO_TOTAL_AMOUNT_MESSAGE)


class NotZeroLottoAmountError(Exception):
    def __init__(self):
        super().__init__(InputMessage.INPUT_NOT_ZERO_LOTTO_TOTAL_AMOUNT_MESSAGE)


def input_purchased_lotto_total_amount():
    while True:
        try:
            lotto_total_amount = int(input(InputMessage.INPUT_PURCHASED_LOTTO_TOTAL_AMOUNT_MESSAGE))
            if is_over_minimum_lotto_total_amount(lotto_total_amount):
                return lotto_total_amount
        except ValueError:
            print(InputMessage.INPUT_INVALID_FORMAT_LOTTO_TOTAL_AMOUNT_MESSAGE)
        except Exception as e:
            print(e)


def is_over_minimum_lotto_total_amount(lotto_total_amount):
    if lotto_total_amount == INPUT_ZERO_TO_LOTTO_AMOUNT:
        raise NotZeroLottoAmountError

    if lotto_total_amount < 1000:
        raise NotSatisfyMinimumAmountError

    return True
