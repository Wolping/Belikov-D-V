# -- coding: utf-8 --

def m():
    p=1
    l = 0
    x = int(input("Введите число - "))
    c= x
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if p!=0:
            if x > c :
                l += 1
            else:
                p=0
        c = x
    print(l)

m()
