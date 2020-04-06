'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''
revenue = input("Введите Вашу выручку - ")
costs = input("Введите Ваши расходы - ")

if (int(revenue) < int(costs)):  # Фирма убыточна
    print("No money, but you hold on!")
elif (int(revenue) == int(costs)):  # Фирма вышла в ноль
    print("Not bad! You`re in the game yet.")
else:  # Фирма в плюсе
    print("Winner, winner! Chicken dinner!")
    profit = float(revenue) - float(costs)
    profitability = profit / float(revenue)
    print(f'Рентабельность Вашей фирмы составила {profitability:.2%}')
    stuff = input("Введите количество персонала - ")
    profit_stuff = profit / int(stuff)
    print(f"Прибыль на одного сотрудника равна {profit_stuff:.2f} рублей")


