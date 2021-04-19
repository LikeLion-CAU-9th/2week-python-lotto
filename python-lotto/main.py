from lotto_statistics.lotto_statistics import get_winning_lotto_result
from lotto_ticket.lotto_store import get_automatic_random_lotteries, get_last_week_winning_lotto
from ui.printer import printer_lotto_start_information, printer_automatic_random_lotteries, \
    printer_last_week_winning_lotto


def run():
    printer_lotto_start_information()

    automatic_random_lotteries = get_automatic_random_lotteries()
    printer_automatic_random_lotteries(automatic_random_lotteries)

    last_week_winning_lotto = get_last_week_winning_lotto()
    print(last_week_winning_lotto)
    print(automatic_random_lotteries)
    printer_last_week_winning_lotto(last_week_winning_lotto)

    print(get_winning_lotto_result(automatic_random_lotteries, last_week_winning_lotto))


def main():
    run()


if __name__ == '__main__':
    main()
