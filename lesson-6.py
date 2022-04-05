# 1 задание
# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
                     #
class TrafficLight:
    # атрибуты класса
    __light_color = ['красный', 'желтый', 'зеленый']
    # методы класса
    def running(self):
        i = 0
        while i < 3:
            print(f'Выполняется переключение светофора\n')
            print(f'{TrafficLight.__light_color[i]}')
            if i == 0:
                sleep(7)
            elif i == 2:
                sleep(2)
            elif i == 3:
                sleep(5)
            i += 1
# создаем экземпляр класса
TrafficLight = TrafficLight
# вызываем метод класса
TrafficLight.running(1)

# 2 задание Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asph_mass(self):
        return self._length*self._width


class Mass(Road):
    def __init__(self, _length, _width, weigth):
        super().__init__(_length, _width)
        self.weigth = weigth

a = Mass(25, 1000, 5)
print(a.asph_mass())

# 3 задание Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Ivan', 'Ivanov', 'QA', 130000, 15000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())


# 4 задание  Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_rigth(self):
        return f'Машина {self.name} повернула направо'

    def turn_left(self):
        return f'Машина {self.name} повернула налево'

    def show_speed(self):
        return f'Машина {self.name} едет со скоростью {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

        if self.speed > 60:
            print(f'Машина {self.name} едет с превышением скорости')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')

        if self.speed > 40:
            print(f'Машина {self.name} едет с превышением скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def if_police(self):
        if self.is_police:
            return(f'Машина {self.name} полицейская')
        else:
            return (f'Машина {self.name} не полицейская')


bmw = SportCar(150, 'черная', 'BMW', False)
kia = WorkCar(110, 'белая', 'KIA', True)
porsche = PoliceCar (180, 'красная', 'PORSCHE', True)
mazda = TownCar(125, 'синяя', 'MAZDA', False)
print(bmw.stop())
print(f'{kia.go()} , а {mazda.turn_left()} ')
print(f'{porsche.name} вместе с {bmw.name} ')
print(f'Какая машина полицейская? {porsche.name}? - {porsche.is_police}')
print(f'Какая машина едет с превышением скорости? - {bmw.show_speed()}')
print(mazda.show_speed())


# 5 задание Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрали предмет - {self.title}. Запуск отрисовки'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрали предмет - {self.title}. Запуск отрисовки'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Выбрали предмет - {self.title}. Запуск отрисовки'


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())



