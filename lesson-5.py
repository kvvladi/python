# 1 задание
# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file1.txt', 'w')
line = input('Введите текст \n')
while line:
    file.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

file.close()
file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file1.txt', 'r')
content = file.readlines()
print(content)
file.close()

# 2 задание
# Создать текстовый файл (не программно),
# сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file2.txt', 'r')
content = file.read()
print(f' Файл содержит в себе: \n {content}')
file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file2.txt', 'r')
content = file.readlines()
print(f'Количество строк в файле: \n {len(content)}')
file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file2.txt', 'r')
content = file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i+1}-ой строки {len(content[i])}')
file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file2.txt', 'r')
content = file.read()
content = content.split()
print(f'Общее количество слов в файле: {len(content)}')
file.close()

# 3 задание
# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file3.txt', 'r') as my_f:
    salary = []
    little = []
    my_l = my_f.read().split('\n')
    for i in my_l:
        i = i.split()
        if int(i[1]) < 20000:
            little.append(i[0])
        salary.append(i[1])
print(f'Оклад менее 20 тысяч: {little} , \n Средняя величина дохода сотрудника: {sum(map(int, salary)) / len(salary)}')


# 4 задание Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rusNumb = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file4.txt', 'r') as file:
     for i in file:
         i = i.split(' ', 1)
         new_file.append(rusNumb[i[0]] + '  ' + i[1])
     print(new_file)

with open('file_4_new.txt', 'w') as file_2:
    file_2.writelines(new_file)

# 5 задание
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

my_f = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file5.txt', 'w')
line = input('Введите числа: \n')
while line:
    my_f.writelines(line)
    line = input('Введите числа: \n')
    if not line:
        break

my_f.close()
my_f = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file5.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# 6 задание
# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести его на экран.

my_file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file6.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file6.txt', 'r')
content = my_file.readlines()
print(f'Число строк в файле: {len(content)}')
my_file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file6.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
 print(f'Число символов {i + 1}-ой строки {len(content[i])}')
my_file = open('/Users/kseniavladimirskaa/PycharmProjects/python_geek/file6.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее число слов: {len(content)}')
my_file.close()