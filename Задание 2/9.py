# -- coding: utf-8 --

n = int(input("Введите первую сторону шоколадки в дольках: "))
m = int(input("Введите вторую сторону шоколадки в дольках: "))
k = int(input("Оставшаяся часть в дольках k: "))
if n != m:
    if (n * m > k) and  (k % n == 0 or k % m == 0):
        print("Да")
    else:
        print("Нет")
else:
    print("Ошибка")