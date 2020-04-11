"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"Автомобиль {self.name} поехал "
    def stop(self):
        return f"Автомобиль {self.name} остановился"
    def turn(self, direction):
        return f"Автомобиль {self.name} повернул {direction}"
    def shw_spd(self):
        return f"Скорость автомобиля {self.name} - {self.speed} км/ч"

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        pass
    def shw_spd(self):
        if self.speed > 60:
            return f"ВНИМАНИЕ! Превышение скорости автомобиля {self.name} - {self.speed} км/ч"
        elif self.speed <= 60:
            return f"Скорость автомобиля {self.name} - {self.speed} км/ч"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        pass

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        pass
    def shw_spd(self):
        if self.speed > 40:
            return f"ВНИМАНИЕ! Превышение скорости автомобиля {self.name} - {self.speed} км/ч"
        elif self.speed <= 40:
            return f"Скорость автомобиля {self.name} - {self.speed} км/ч"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        pass

twn_car = TownCar(65, "blue", "Dodge Voyager", False)
sp_car = SportCar(120, "yellow", "Flash McQueen", False)
wrk_car = WorkCar(35, "green", "Ural 4320", False)
plc_car = PoliceCar(105, "white with blue line", "A.C.A.B.", True)

new_list = [twn_car, sp_car, wrk_car, plc_car]
print("*****    ИНФОРМАЦИЯ ОБ АВТОМОБИЛЯХ    *****")
for i in range(len(new_list)):
    print(f"Автомобиль - {new_list[i].name}, цвет - {new_list[i].color}, текущая скорость - {new_list[i].speed}, "
          f"является служебной машиной - {new_list[i].is_police}")

print("*****    ПРИМЕРЫ ДЕЙСТВИЙ С АВТОМОБИЛЯМИ    *****")
print(twn_car.turn("направо"))
print(sp_car.go())
print(plc_car.stop())
print(wrk_car.turn("налево"))
print(twn_car.shw_spd())
print(sp_car.shw_spd())