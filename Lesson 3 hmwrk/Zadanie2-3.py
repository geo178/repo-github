'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

name = input('Введите имя')
surname = input('Введите фамилию')
birthyear = int(input('Введите год рождения'))
city = input('Введите город')
email = input('Введите адрес электронной почты')
telephone = input('Введите номер телефона')

def my_func(name, surname, birthyear, city, email, phone):
    print1(name, surname, birthyear, city, email, phone)

# my_func(name= 'Vladimir', surname='Putin', birthyear=1953, city='Spb', email='email', phone='812')