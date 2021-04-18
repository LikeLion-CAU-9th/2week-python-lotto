PRINTER_INFORMATION_START_POINT = "> "


def printer_format(func):
    def wrapper():
        print(PRINTER_INFORMATION_START_POINT, end='')
        func()
        print(sep='\n')

    return wrapper
