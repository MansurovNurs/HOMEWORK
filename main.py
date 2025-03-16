from logic import find_number
from termcolor import cprint

def main():
    result = find_number()  # Запуск игры
    cprint(result, 'red', 'on_cyan')  # Выводим результат игры с цветами

if __name__ == "__main__":
    main()
