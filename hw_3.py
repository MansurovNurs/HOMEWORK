class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, value):
        self.__cpu = value

    def get_memory(self):
        return self.__memory

    def set_memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Компьютер: Процессор={self.__cpu}, Память={self.__memory}ГБ"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards):
        self.__sim_cards_list = sim_cards

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            print(f"Звонок на {call_to_number} с SIM-{sim_card_number} ({self.__sim_cards_list[sim_card_number - 1]})")
        else:
            print("Ошибка: Неверный номер SIM-карты.")

    def __str__(self):
        return f"Телефон: SIM-карты: {', '.join(self.__sim_cards_list)}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"Смартфон: Процессор={self.get_cpu()}, Память={self.get_memory()}ГБ, SIM-карты: {', '.join(self.get_sim_cards_list())}"

# Создание объектов
computer = Computer(3.5, 16)
phone = Phone(["Beeline", "MegaCom"])
smartphone1 = SmartPhone(2.8, 8, ["O!", "Beeline"])
smartphone2 = SmartPhone(3.0, 12, ["MegaCom", "O!"])

# Вывод информации
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Проверка методов
print("Результат вычислений:", computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Центральная площадь")

# Проверка магических методов
print("Компьютер == Смартфон1:", computer == smartphone1)
print("Компьютер > Смартфон1:", computer > smartphone1)
