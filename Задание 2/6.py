# -- coding: utf-8 --

str1 = int(input("Номер строки первой клетки:"))
stolbec1 = int(input("Номер столбца первой клетки:"))
str2 = int(input("Номер строки второй клетки:"))
stolbec2 = int(input("Номер столбца второй клетки:"))
if ((str1 and stolbec1) >= 1 and (str1 and stolbec1) <= 8) and ((str2 and stolbec2) >= 1 and (str2 and stolbec2) <= 8):
    if (str1 % 2 == 1 and stolbec1 % 2 == 1) or (str1 % 2 == 0 and stolbec1 % 2 == 0) :
        colour1 = str("Белый")
    else:
        colour1 = str("Черный")
    if (str2 % 2 == 1 and stolbec2 % 2 == 1) or (str2 % 2 == 0 and stolbec2 % 2 == 0):
        colour2 = str("Белый")
    else:
        colour2 = str("Черный")
else:
    print("Ошибка")
if colour1 == colour2:
    print("Да")
else:
    print("Нет")