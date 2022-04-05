# 1 задание
# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        list = []
        for i in a:
            list.append([j for j in i])
        self.a = list

    def __str__(self):
        # перегрузка метода для вывода матрицы
        self.c = str(self.a)
        return self.c

    def __add__(self, other):
        # перегрузка метода для сложения двух объектов класса двух матриц (Matrix)
        result = []
        numb = []
        # добавление матрицы с использованием вложенного цикла for
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                sum = other.a[i][j] + self.a[i][j]
                numb.append(sum)
                if len(numb) == len(self.a):
                    result.append(numb)
                    numb = []
        return Matrix(result)


m1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
m2 = Matrix([[13, 1, -4], [17, 17, -1], [-1, -9, 10]])
print(m1 + m2)
print(m1 + m2)

# 2 задание
# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Clothers:
    def __init__(self, size, heigth):
        self.size = size
        self.heigth = heigth

    def material_consumption_1(self):
        return self.size/6,5 + 0,5

    def material_consumption_2(self):
        return 2*self.heigth + 0,3

    @property
    def material_consumption_res(self):
        return str(f'Общий расход ткани составляет: {self.size/6,5 + 0,5} + {2 * self.heigth + 0, 3}')


class Coat(Clothers):
    def __init__(self, size, heigth):
        super().__init__(size, heigth)
        self.material_4coat = self.size/6,5 + 0,5

    def __str__(self):
        return f'Размер ткани на пальто: {self.material_4coat}'



class Costume(Clothers):
    def __init__(self, size, heigth):
        super().__init__(size, heigth)
        self.material_4costume = 2*self.heigth + 0,3

    def __str__(self):
        return f'Размер ткани на костюм: {self.material_4costume}'

a = Coat(5, 2)
b = Costume(3,8)
print(a)
print(b)
print(a.material_4coat)
print(b.material_4costume)
print(a.material_consumption_1())
print(b.material_consumption_2())
print(a.material_consumption_res)

# задание 3
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if (self.amount - other.amount) > 0:
            return Cell(self.amount - other.amount)
        else:
            return f'Разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return Cell(int(self.amount * other.amount))


    def __truediv__(self, other):
        return Cell(round(self.amount // other.amount))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.amount // cells_in_row):
            row += str(f'{"*" * self.amount} \\n')
            row += str(f'{"*" * (self.amount % cells_in_row)}')
            return row

    def __str__(self):
        return str(f'В клетке {self.amount * "*"} ячеек')


a = Cell(13)
b = Cell(4)
print(a)
print(b)
print(a + b)
print(a - b)
print(a.make_order(8))
print(b.make_order(22))
