"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f"Запуск отрисовки через родительский класс c помощью {self.title}."

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass
    def draw(self):
        return f"Запуск отрисовки с уникальным тегом #PEN через дочерний класс c помощью {self.title}."

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass
    def draw(self):
        return f"Запуск отрисовки с уникальным тегом #PENCIL через дочерний класс c помощью {self.title}."

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass
    def draw(self):
        return f"Запуск отрисовки с уникальным тегом #HANDLE через дочерний класс c помощью {self.title}."

new_list = [Pen("pen"), Pencil("pencil"), Handle("handle")]
print("*****    ИНФОРМАЦИЯ ОБ МЕТОДАХ ЗАРИСОВКИ    *****")
for i in range(len(new_list)):
   print(f"предмет - {new_list[i].title}, способ - {new_list[i].draw()}")
