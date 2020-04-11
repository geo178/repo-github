"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def user(**kwargs): return (f"Пользователь {kwargs['name']} {kwargs['surname']}, "
                            f"рожденный {kwargs['bdate']} года, живет в городе {kwargs['city']}. "
            f"Можно связаться по телефону {kwargs['phone']} или e-mail {kwargs['email']}.")
u_data = False

while not u_data:
    try:
        u_data = 'Владимир Путин, 07.10.1952, Москва, mr_president@kreml.ru, 89997779977'.split()
         
    except IndexError:
        u_data = False
        def user(**kwargs):
            return (f'Пользователь {kwargs["name"]} {kwargs["surname"]}, '
                    f'рожденный {kwargs["bdate"]} года, живет в городе {kwargs["city"]}. \
        Можно связаться по телефону {kwargs["phone"]} или e-mail {kwargs["email"]}.')
        u_data = False

        while not u_data:
            try:
                u_data = 'Владимир Путин, 07.10.1952, Москва, mr_president@kreml.ru, 89997779977'.split()
            except IndexError:
                u_data = False
                print('Не корректный ввод.')
            try:
                u = user(name=u_data[0], surname=u_data[1], bdate=u_data[2], city=u_data[3], email=u_data[4],
                         phone=u_data[5])
            except IndexError:
                print(f'Количество данных не соответствует запросу.')
                u_data = False
            print(u)
        print('Goodbye!!!')

        try:
            u = user(name=u_data[0], surname=u_data[1],
                         bdate=u_data[2],  city=u_data[3],
                         email=u_data[4],  phone=u_data[5])
        except IndexError:
                print(f'Количество данных не соответствует запросу.')
                u_data = False
                print(u)
print('Goodbye!!!')