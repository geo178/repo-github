'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
'''
userinput = input('Введите элементы разделяя их пробелом: ').split()

for i in range (len(userinput)):
    if len(userinput[i]) <= 10:
        print(i + 1, userinput[i])
    else:
        print(i + 1, (userinput[i])[:10])