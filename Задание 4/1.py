# -- coding: utf-8 --
def z():
    s = input("")
    print(s[2])
    print(s[-2])
    print(s[0:5])
    print(s[:-2])
    print(s[0:: 2])
    print(s[1: :2])
    print(s[::-1])
    s = s [::-1]
    print(s[0:: 2])
    print(len(s))
z()