# -- coding: utf-8 --
def z():
    s = input("")
    s = s[:s.find("h")] + s[s.rfind("h")+1:]
    print(s)
z()
