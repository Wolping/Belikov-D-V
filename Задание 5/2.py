# -*- coding: utf-8 -*-

def m():
    a = 2
    b = int(input("Введите число больше 2 - "))
    while b % a != 0:
        a += 1
    print(a)
m()