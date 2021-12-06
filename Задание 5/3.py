# -*- coding: utf-8 -*-

def m():
    a = 2
    d = 2
    c = 1
    b = int(input("Введите число - "))

    while d * a < b:
        d *= a
        c+=1
    print(d)
    print(c)

m()
        