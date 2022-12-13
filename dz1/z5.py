# Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
def coord_input():
    x = float(input())
    y = float(input())
    return x,y


x1,y1 = coord_input()
x2,y2 = coord_input()

d = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

print(f"{d: .3}")
