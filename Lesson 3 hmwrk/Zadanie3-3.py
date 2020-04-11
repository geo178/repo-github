"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
def my_func(a,  b, c):
    sum = float(a) if float(a) > float(b) else float(b)
    sum += float(a) if float(a) > float(c) else float(c)
    return sum
print(my_func('36', '87.911',  '86.19'))
print('Ciao!!!')