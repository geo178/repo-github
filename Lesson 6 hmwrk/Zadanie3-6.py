"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position:
    def __init__(self, worker):
        self.worker = worker
    def get_full_name(self):
        return f"{self.worker.name}, {self.worker.surname}"
    def get_total_income(self):
        return f"Доход составляет - {self.worker._income['wage'] + self.worker._income['bonus']} рублей."


matrix = [
            ["Vladimir", "Putin", "Mr. President", 9000, 2000],
            ["Vitya", "Zolotov", "Director firmy", 7000, 3000],
            ["Vladimir", "Kolokoltsev", "Mr. Policeman", 7000, 4000],
            ["Dima", "Medvedev", "Deneg net, no vy derjites", 0, 0],
            ["Ivan", "Grozniy", "Tsar", 1000000, 12000]
         ]

for i in range(len(matrix)):
    people = Worker(matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3],matrix[i][4])
    print(Position(people).get_full_name(), Position(people).get_total_income())
