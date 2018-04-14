from colorama import init, Fore, Back, Style
import os


class Console:

    @classmethod
    def init(cls):
        init(convert=True, strip=False)

    @classmethod
    def warn(cls, message):
        cls.write(message, Fore.YELLOW)

    @classmethod
    def error(cls, message):
        cls.write(message, Fore.RED)

    @classmethod
    def write(cls, message, *formats):
        print(f"{''.join(formats)}{message}{Style.RESET_ALL}")

    @classmethod
    def clear(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
