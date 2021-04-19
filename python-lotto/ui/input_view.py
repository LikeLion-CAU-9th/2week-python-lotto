from lotto_ticket.lotto_information import LottoInformation
from ui.printer import printer_value_error_message, PrintErrorMessage, printer_exception_error_message

INPUT_ZERO_TO_LOTTO_AMOUNT = 0


class InputMessage:
    INPUT_PURCHASED_LOTTO_TOTAL_AMOUNT_MESSAGE = '로또 구입 금액을 입력해주세요: '
    INPUT_LAST_WEEK_WINNING_LOTTO_MESSAGE = '지난주 당첨 번호를 입력해주세요'


class NotSatisfyMinimumAmountError(Exception):
    def __init__(self):
        super().__init__(PrintErrorMessage.INPUT_NOT_SATISFY_MINIMUM_LOTTO_TOTAL_AMOUNT_MESSAGE)


class NotZeroLottoAmountError(Exception):
    def __init__(self):
        super().__init__(PrintErrorMessage.INPUT_NOT_ZERO_LOTTO_TOTAL_AMOUNT_MESSAGE)


class UnderSixNumberInLottoError(Exception):
    def __init__(self):
        super().__init__(PrintErrorMessage.INPUT_UNDER_SIX_NUMBER_IN_LOTTO_MESSAGE)


class OverSixNumberInLottoError(Exception):
    def __init__(self):
        super().__init__(PrintErrorMessage.INPUT_OVER_SIX_NUMBER_IN_LOTTO_MESSAGE)


def input_purchased_lotto_total_amount():
    while True:
        try:
            lotto_total_amount = int(input(InputMessage.INPUT_PURCHASED_LOTTO_TOTAL_AMOUNT_MESSAGE))
            if is_over_minimum_lotto_total_amount(lotto_total_amount):
                return lotto_total_amount
        except ValueError:
            printer_value_error_message()
        except Exception as e:
            printer_exception_error_message(e)


def is_over_minimum_lotto_total_amount(lotto_total_amount):
    if lotto_total_amount == INPUT_ZERO_TO_LOTTO_AMOUNT:
        raise NotZeroLottoAmountError
    if lotto_total_amount < LottoInformation.LOTTO_PRICE:
        raise NotSatisfyMinimumAmountError
    return True


def input_last_week_winning_lotto():
    while True:
        try:
            last_week_winning_lotto = input(InputMessage.INPUT_LAST_WEEK_WINNING_LOTTO_MESSAGE)
            last_week_winning_lotto_ticket = last_week_winning_lotto.split(",")
            if has_six_number(last_week_winning_lotto_ticket):
                return last_week_winning_lotto
        except Exception as e:
            print(e)


def has_six_number(last_week_winning_lotto):
    if len(last_week_winning_lotto) < 6:
        raise UnderSixNumberInLottoError
    if len(last_week_winning_lotto) > 6:
        raise OverSixNumberInLottoError
    return True
