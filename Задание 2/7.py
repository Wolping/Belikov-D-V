# -- coding: utf-8 --

g = int(input("Введите год"))
if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
    print("Да")
else:
    print("Нет")