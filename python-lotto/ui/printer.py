from lotto_decorator.printer_decorator import printer_format
from lotto_statistics.lotto_statistics import LottoStatisticMatchingNumber

DECIMAL_POINT_OUT_RANGE = 2


class PrintMessage:
    PRINTER_LOTTO_START_MESSAGE = "로또 게임을 시작합니다!"
    PRINTER_AUTOMATIC_RANDOM_LOTTERIES_MESSAGE = "{}장의 로또를 구입하셨습니다."
    PRINTER_WINNING_LOTTO_STATISTICS_MESSAGE = "로또 당첨 결과"
    PRINTER_WINNING_LOTTO_STATISTICS = "{}등({}개가 맞을 때) - {}원 - {}개"
    PRINTER_LOTTO_PROFIT_MESSAGE = "수익률"


class PrintErrorMessage:
    INPUT_INVALID_FORMAT_LOTTO_TOTAL_AMOUNT_MESSAGE = '숫자형식의 금액을 입력해주세요.'
    INPUT_NOT_ZERO_LOTTO_TOTAL_AMOUNT_MESSAGE = '구입할 로또 금액으로 0원을 입력하실 수 없습니다. 로또 한장 이상의 금액을 입력해주세요.'
    INPUT_NOT_SATISFY_MINIMUM_LOTTO_TOTAL_AMOUNT_MESSAGE = "로또 한장 이상의 금액을 입력해주세요."
    INPUT_UNDER_SIX_NUMBER_IN_LOTTO_MESSAGE = '6개 미만으로 입력하셨습니다. 숫자 6개를 입력해주세요.'
    INPUT_OVER_SIX_NUMBER_IN_LOTTO_MESSAGE = '6개 초과로 입력하셨습니다. 숫자 6개를 입력해주세요.'
    NOT_DUPLICATED_NUMBER_IN_LOTTO_MESSAGE = '중복되는 숫자를 입력하실 수 없습니다.'
    INVALID_NUMBER_RANGE_IN_LOTTO_MESSAGE = "1 ~ 45 까지의 숫자를 입력해주세요."


@printer_format
def printer_lotto_start_information():
    print(PrintMessage.PRINTER_LOTTO_START_MESSAGE)


@printer_format
def printer_automatic_random_lotteries(lotteries: list):
    print(PrintMessage.PRINTER_AUTOMATIC_RANDOM_LOTTERIES_MESSAGE.format(len(lotteries)))

    for lotto in lotteries:
        print(lotto)


@printer_format
def printer_exception_error_message(error_message):
    print(error_message)


@printer_format
def printer_value_error_message():
    print(PrintErrorMessage.INPUT_INVALID_FORMAT_LOTTO_TOTAL_AMOUNT_MESSAGE)


@printer_format
def printer_last_week_winning_lotto(last_week_winning_lotto):
    print(last_week_winning_lotto)


@printer_format
def printer_winning_lotto_statistics_information_message():
    print(PrintMessage.PRINTER_WINNING_LOTTO_STATISTICS_MESSAGE)


def printer_winning_lotto_statistics(winning_lotto_result: dict):
    for lotto_matched_index in LottoStatisticMatchingNumber:
        print(PrintMessage.PRINTER_WINNING_LOTTO_STATISTICS.format(
            lotto_matched_index.rank,
            lotto_matched_index.matched_count,
            lotto_matched_index.price,
            winning_lotto_result[lotto_matched_index.matched_count]
        ))


@printer_format
def printer_lotto_profit_information_message():
    print(PrintMessage.PRINTER_LOTTO_PROFIT_MESSAGE)


def printer_lotto_profit(profit: float):
    print(round(profit, DECIMAL_POINT_OUT_RANGE))
