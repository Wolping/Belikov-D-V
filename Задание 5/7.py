# -- coding: utf-8 --

def m():
    l = 0
    x = int(input("Введите число - "))
    c= x
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if x > c :
            l += 1
        c = x
    print(l)

m()
