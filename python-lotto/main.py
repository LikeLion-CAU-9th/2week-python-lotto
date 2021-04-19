from lotto_statistics.lotto_statistics import get_winning_lotto_result
from lotto_statistics.profit import get_lotto_profit
from lotto_ticket.lotto_store import get_automatic_random_lotteries, get_last_week_winning_lotto
from ui.printer import printer_lotto_start_information, printer_automatic_random_lotteries, \
    printer_last_week_winning_lotto, printer_winning_lotto_statistics_information_message, \
    printer_winning_lotto_statistics


def run():
    printer_lotto_start_information()

    automatic_random_lotteries, purchased_lotto_total_amount = get_automatic_random_lotteries()
    printer_automatic_random_lotteries(automatic_random_lotteries)

    last_week_winning_lotto = get_last_week_winning_lotto()
    printer_last_week_winning_lotto(last_week_winning_lotto)

    printer_winning_lotto_statistics_information_message()
    winning_lotto_result = get_winning_lotto_result(automatic_random_lotteries, last_week_winning_lotto)
    printer_winning_lotto_statistics(winning_lotto_result)

    print(get_lotto_profit(winning_lotto_result, purchased_lotto_total_amount))


def main():
    run()


if __name__ == '__main__':
    main()
