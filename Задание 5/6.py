# -*- coding: utf-8 -*-

def m():
    a = 1
    s = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        a+=1
        s += x
    print(s / a)

m()
