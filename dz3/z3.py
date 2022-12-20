# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input("Введите кол-во элементов списка "))
a = [round(random.random()*100  , 2)for i in range (n)]
print(a)

max = 0
min = (a[0]*100)%100
for i in a:
  if (i*100)%100 > max:
    max = (i*100)%100
  if (i*100)%100 < min:
    min = (i*100)%100
print("Разница между максимальным и минимальным значением дробной части элементов =",  round((max-min)/100, 3))