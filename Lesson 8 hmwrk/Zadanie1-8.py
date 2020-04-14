"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def extract(cls, date):
        print(cls, date)
        my_date = []

        for i in date.split():
            if i != "/":
                my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    # print(cls, param, Data(12).par)

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return f"Okay"
                else:
                    return f"Неправильно введен год"
            else:
                return f"Такого месяца не существует"
        else:
            return f"Неправильно введен день"

    def __str__(self):
        return f"Сегодня {Data.extract(self.date)}"

today = Data("13 / 04 / 2020")
print(today)
print(Data.valid(22, 11, 2078))
print(today.valid(13, 4, 2011))
print(Data.extract("19 / 8 / 2012"))
print(today.extract("22 / 5   / 2020"))
print(Data.valid(9, 11, 2001))
