'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

# m_dict = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
#           7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

m_list = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
m_seasons = ["winter", "winter", "spring", "spring", "spring", "summer",
          "summer", "summer", "autumn", "autumn", "autumn", "winter"]

m_dict = {
            1:{"mouth":"january", "season":"winter"},
            2:{"mouth":"february", "season":"winter"},
            3:{"mouth":"march", "season":"spring"},
            4:{"mouth":"april", "season":"spring"},
            5:{"mouth":"may", "season":"spring"},
            6:{"mouth":"june", "season":"summer"},
            7:{"mouth":"july", "season":"summer"},
            8:{"mouth":"august", "season":"summer"},
            9:{"mouth":"september", "season":"autumn"},
            10:{"mouth":"october", "season":"autumn"},
            11:{"mouth":"november", "season":"autumn"},
            12:{"mouth":"december", "season":"winter"}
          }

def math():
    m = int(input('Введите месяц цифрами - '))
    if m > 12 or m < 1:
        print("Incorrect input")
        math()
    else:
        for month in m_dict:
            if month == m:
                print(f"{month} month of the year is {m_dict[month]['mouth']} ({m_dict[month]['season']})")
                print(f"{month} month of the year is {m_list[month - 1]} ({m_seasons[month - 1]})")
math()




