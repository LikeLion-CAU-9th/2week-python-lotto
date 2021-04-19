from lotto_ticket.lotto_store import get_automatic_random_lotteries
from ui.printer import printer_lotto_start_information, printer_automatic_random_lotteries


def run():
    printer_lotto_start_information()
    printer_automatic_random_lotteries(get_automatic_random_lotteries())


def main():
    run()


if __name__ == '__main__':
    main()
