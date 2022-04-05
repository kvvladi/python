# задание 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_numb(*args):

     try:
         arg1 = int(input("Введите делитель: "))
         arg2 = int(input("Введите делимое "))
         res = arg1 / arg2
     except ValueError:
         return 'Value error'
     except ZeroDivisionError:
         return "Неверное число. На ноль делить нельзя."

     return res

print(f'Результат:  {my_numb()}')

# задание 2
# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Введите свое имя: ')
secondName = input('Введите свою фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите свой e-mail: ')
phone = input('Введите номер телефона: ')
def user_data(name, secondName, year, city, email, phone):

    return(''.join([name, secondName, year, city, email, phone]))

print(user_data(name = name, secondName = secondName, year = year, city = city, email = email, phone = phone))

# задание 3
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат - {my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))}')


# задание 4
# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

# 1 вариант
def my_func(x,y):
    x = int(input('Введите аргумент х: '))
    y = int(input('Введите аргумент y: '))

    if x < 0:
        return ValueError('Неверный аргумент для x')

    if int(y) != float(y) or y >= 0:
        return ValueError('Неверный аргумент для y')

    return (x ** y)

print(my_func(2, -4))

# 2 вариант
def power(a,n):
    a = int(input('Введите аргумент х: '))
    n = int(input('Введите аргумент y: '))

    if a == 0:
        return 0
    if n < 0:
        a= 1.0/a
        n= -n
        res= 1
    while n > 0:
        res= res * a
        n= n-1
    return res

print ("power(a,n)", power(a,n), a**n)


# задание 5
# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def my_sum():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Введите символ Z для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'z' or number[el] == 'Z':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'сумма равна {sum_res}')
    print(f'итоговая сумма равна {sum_res}')


my_sum()

# задание 6
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def func(a):
    return a.title()

print(func("abca dsd"))