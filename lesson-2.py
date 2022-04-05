# Задание 1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

data_list = ['Hello', 'user', 13, ' ', 17,3, None]
print(type(data_list))

# Задание 2
# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

user_list = int(input("Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < user_list:
    my_list.append(input("Введите элемент списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

# Задание 3
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.


season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите число месяца: ") )

if month == 1 or month == 12 or month == 2:
    print(season_dict.get(1))
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    input("Такого месяца не существует")

# Задание 4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

line = input("Введите строку из нескольких слов: ")
word = []
number = 1

for el in range(line.count(' ') + 1):
    word = line.split(' ')
    if len(str(word)) <= 10:
        print (f" {number} {word[el]}")
        number += 1
    else:
        print(f" {number} {word[0:10]}")
        number += 1

my_str = input("Введите строку из нескольких словами: ")
my_word = my_str.split(' ')
for i, el in enumerate(my_word, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")

#2-ой способ
my_str = input("Введите строку с несколькими словами: ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
     my_word = my_str.split()
     if len(str(my_word)) <= 10:
         print(f" {num} {my_word [el]}")
         num += 1
     else:
         print(f" {num} {my_word [el] [0:10]}")
         num += 1


# Задание 5
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

new_number = int(input("Введите новое число: "))
my_list = [7, 4, 3, 2]
a = my_list.count(new_number)
for element in my_list:
     if a > 0:
         i = my_list.index(new_number)
         my_list.insert(i+a, new_number)
         break
     else:
         if new_number > element:
             n = my_list.index(element)
             my_list.insert(n, new_number)
             break
         elif new_number < my_list[len(my_list) - 1]:
             my_list.append(new_number)
print(my_list)