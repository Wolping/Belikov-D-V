# -- coding: utf-8 --

a = int(input("Расстояния между рядами с дырочками"))
b = int(input("Расстояние между дырочками в ряду"))
l = int(input("Длинна оставшегося шнурка"))
N = int(input("Кол-во дырочек в ряду"))
def shnurok(a , b , l, N):
	return (b*(N-1))*2 + (N*2-1)*a + l*2
print("Длинна всего шнурка равна:",shnurok(a, b, l, N))