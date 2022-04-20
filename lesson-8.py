# 1 задание
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def to_int(cls, data):
        my_data = []
        for i in data.split():
            if i!= '-' :
                data.append(i)
        return(int(my_data[0]), int(my_data[1], int(my_data[2])))


    @staticmethod
    def data_valid(day, month, year):
        if i <= day >=31:
            if i <= month >=12:
                if 2022 >= year >= 0:
                    return f'Корректная дата'
                else:
                    return f'Некорретный год'
            else:
                return f'Некорректный месяц'
        else:
            return f'Некорретный день'

    def __str__(self):
        return f'Текущая дата: {Data.extract(self.data)}'


current = Data('08-04-2022')
print(current)
print(Data.valid(13, 13, 2020))
print(current.valid('08, 04, 2022'))
print(Data.extract('08-04-2022'))


# 2 задание
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroDevision:
    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    @staticmethod
    def zero_devision(numb1, numb2):
        try:
            return numb1 / numb2
        except:
            print("Деление на ноль недопустимо")

a = ZeroDevision(13, 40)
print(ZeroDevision.zero_devision(50, 0))
print(ZeroDevision.zero_devision(0, 12))
print(a.zero_devision(50, 0))

# 3 задание
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class ListOnluNumb(ValueError):
    pass


list = []

while True:
    try:
        value = input('Добавьте в список число:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise ListOnluNumb(value)
        list.append(int(value))
    except ListOnluNumb as ex:
        print('Это не число."', ex)
print(list)

# 5 задание
# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


class OrgTech:
    def __init__(self, name, amount, type):
        self.name = name
        self.amount = amount
        self.type = type
        self.printer = {}
        self.xerox = {}

    def __str__(self):
        return f'Наименование оргтехники: {self.name}, количество единиц: {self.amount}, тип оргтехники: {self.type}'

    @classmethod
    def priem_tech(self, name, amount, type):
        return f'Начинаем прием оргтехники --> Наименование: {self.name}, количество единиц: {self.amount}, тип оргтехники: {self.type}'

org =  OrgTech('printer', 33, 'Canon')
print(org)

# 6 задание
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class OrgTechGeneral:
    def __init__(self, name, amount, type, price, *args):
        self.name = name
        self.amount = amount
        self.type = type
        self.price = price
        self.store_res = []
        self.store = []
        self.data = {'Название устройства': self.name, 'Тип устройства': self.type, 'Цена за ед': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.amount}'

    def validation(self):
        try:
            data = input(f'Введите наименование ')
            data_p = int(input(f'Введите цену за ед '))
            data_am = int(input(f'Введите количество '))
            unique = {'Модель устройства': data, 'Цена за ед': data_p, 'Количество': data_am}
            self.data.update(unique)
            self.store.append(self.data)
            print(f'Список устройств -\n {self.store}')
        except:
            return f'Ошибка при вводе данных'

        print(f'Для выхода нажмите Q, для продолжения - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.store_res.append(self.store)
            print(f'Итого в складе -\n {self.store_res}')
            return f'Выход'
        else:
            return OrgTechGeneral.validation(self)

class Printer(OrgTechGeneral):
    def to_print(self):
        return f'Печать {self.amount} копий'

class Scanner(OrgTechGeneral):
    def to_scan(self):
        return f'Сканирование {self.amount} раз'

class Copier(OrgTechGeneral):
    def to_copier(self):
        return f'Копирование  {self.amount} раз'

unit_1 = Printer('samsung', 1500, 3, 9)
unit_2 = Scanner('Canon', 1800, 5, 7)
unit_3 = Copier('Xerox', 900, 3, 13)
print(unit_1.validation())
print(unit_2.validation())
print(unit_3.validation())
print(unit_1.to_print())
print(unit_3.to_copier())

# 7 задание
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.intent = a + b *i

    def __add__(self, other):
        print('Cуммы равна: ')
        return f'intent = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print('Произведение равно: ')
        return f'intent = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'intent = {self.a} + {self.b} * i'

m = ComplexNumber(14, 2)
n = ComplexNumber(-5, 6)
print(m)
print(m + n)
print(m * n)