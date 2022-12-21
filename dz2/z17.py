# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def file_read(path):
    data = open(os.path.join(__location__, path), 'r')
    a = [int(line) for line in data]
    data.close()    
    return a

position = file_read('file.txt')

n = int(input("Введите число: "))
list = [i for i in range(-n,n+1)]

print(f"{list}")

proiz = 1
for i in position:
    if i < len(list):
        proiz *= list[i]
        print(f"Позиция: {i}  Элемент в этой позиции: {list[i]}")

print(f"Их произведение: {proiz}")      


