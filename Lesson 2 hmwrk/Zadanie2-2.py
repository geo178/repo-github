'''
Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

result = []
a_list = input('Введите элементы разделяя их пробелами: ').split()
l1 = a_list[::2]
l2 = a_list[1::2]
for i in range(len(l2)):
	result.append(l2[i])
	result.append(l1[i])
if len(l1) != len(l2):
	result.append(l1[-1])
print(f'Список пользователя:\t{a_list}')
print(f'Результат:\t\t{result}')



