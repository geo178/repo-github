"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
with open("salary.txt", "r") as my_file:
    salary = []
    less_20 = []
    my_list = my_file.read().split('\n')
    for s in my_list:
        s = s.split()
        if int(s[1]) < 20000:
           less_20.append(s[0])
        salary.append(s[1])
print(f"Оклад меньше 20.000 {less_20}, "
      f"средний оклад {sum(map(int, salary)) / len(salary)}")