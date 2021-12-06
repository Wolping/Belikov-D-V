# -*- coding: utf-8 -*-

def m():
    c = 1
    m = 0
    l = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if(l != 0):
    
            if(x == p):
                c += 1
            else:
                if(m < c):
                    m = c
                c = 1
        p = x
        l+=1
    print(max(m, c))

m()
