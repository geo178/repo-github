'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''
new_list = [False, "Again", 25, 2.1, True, [1, 2, 3, 4,], -16]

for i in range(len(new_list)):
    print(f"{i + 1} {new_list[i]} {type(new_list[i])}")
