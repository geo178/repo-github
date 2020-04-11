"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import sys
import time

class TrafficLight:
    color = "red"
    def running(self):
        while True:
            sys.stderr.write(f"\r")
            sys.stderr.write(f"{self.color}")
            time.sleep(7)
            sys.stderr.write(f"\r")
            self.color = "yellow"
            sys.stderr.write(self.color)
            time.sleep(2)
            sys.stderr.write(f"\r")
            self.color = "green"
            sys.stderr.write(self.color)
            time.sleep(5)
            sys.stderr.write(f"\r")
            self.color = "red"

TrafficLight().running()
