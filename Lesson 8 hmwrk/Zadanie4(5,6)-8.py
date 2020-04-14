"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад
и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад,
нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
"""
class TechStore:
    def __init__(self, name, price, quantity, num_list, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.num_list = num_list
        self.store_full = []
        self.store = []
        self.my_dict = {"Наименование товара": self.name, "Цена": self.price, "Количество": self.quantity}

    def __str__(self):
        return f"{self.name} цена {self.price} количество {self.quantity}"

    def reception(self):
        try:
            unit_n = input(f"Введите наименование товара")
            unit_p = input(f"Введите наименование товара")
            unit_q = input(f"Введите наименование товара")
            unique = {'Модель устройства': unit_n, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_dict.update(unique)
            self.store.append(self.my_dict)
            print(f'Текущий список -\n {self.store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.store_full.append(self.store)
            print(f'Весь склад -\n {self.store_full}')
            return f'Выход'
        else:
            return TechStore.reception(self)


        pass
class Printer(TechStore):
    def to_print(self):
        return f'to print something {self.numb} times'

class Scanner(TechStore):
    def to_scan(self):
        return f'to scan something {self.numb} times'

class Xerox(TechStore):
    def to_copy(self):
        return f'to copy something {self.numb} times'

unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Xerox('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copy())



















