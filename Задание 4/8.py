# -- coding: utf-8 --
def z():
    s = input("")
    s = s[s.find("h")+1 : s.rfind("h")]
    print(s[::-1])
z()
