# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def file_read(path):
    a = []
    data = open(os.path.join(__location__, path), 'r')
    for line in data:
        a.append(int(line))
    data.close()    
    return a

position = file_read('file.txt')

n = int(input("Введите число: "))
list = []
for i in range(-n,n+1):
    list.append(i)

print(f"{list}")

proiz = 1
for i in position:
    if i < len(list):
        proiz *= list[i]
        
for i in position:
    print(f"Позиция: {i}  Элемент в этой позиции: {list[i]}")

print(f"Их произведение: {proiz}")      


