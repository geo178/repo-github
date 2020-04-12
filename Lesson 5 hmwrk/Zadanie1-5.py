"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
my_func = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_func.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_func.close()
my_func = open('test.txt', 'r')
content = my_func.readlines()
print(content)
my_func.close()