PRINTER_INFORMATION_START_POINT = "> "


def printer_format(func):
    def wrapper(*args):
        print(PRINTER_INFORMATION_START_POINT, end='')
        func(*args)
        print(sep='\n')

    return wrapper
