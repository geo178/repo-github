"""
Представлен список чисел.
Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint

def generators(f_num, s_num, amount):
    result = []
    for i in range(amount):
        result.append(randint(f_num, s_num))
    return result
my_list = generators(0, 10, 10)
n_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        n_list.append(my_list[i])
print(f"Случайно созданный список чисел - {my_list}")
print(f"Выборка из созданного списка чисел - {n_list}")

