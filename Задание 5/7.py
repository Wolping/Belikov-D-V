# -*- coding: utf-8 -*-

def m():
    c = 0
    l = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if(l != 0):
            if(x > c):
                c += 1
        c = x
        l+=1
    print(c)

m()
