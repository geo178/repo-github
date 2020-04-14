"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""
class DivisionByNull:
    def __init__(self, divider, dominator):
        self.divider = divider
        self.dominator = dominator

    @staticmethod
    def divideby_0(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")

division = DivisionByNull(20, 200)
print(division.divideby_0(110, 0))