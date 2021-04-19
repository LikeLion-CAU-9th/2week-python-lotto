from lotto_ticket.lotto_store import get_automatic_random_lotteries, get_last_week_winning_lotto
from ui.printer import printer_lotto_start_information, printer_automatic_random_lotteries, \
    printer_last_week_winning_lotto


def run():
    printer_lotto_start_information()
    printer_automatic_random_lotteries(get_automatic_random_lotteries())
    printer_last_week_winning_lotto(get_last_week_winning_lotto())


def main():
    run()


if __name__ == '__main__':
    main()
