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
if position[0] < len(list) and position[1] < len(list):
    sum = list[position[0]] + list[position[1]]
    print(f"Позиции элементов {position[0]} и {position[1]}")
    print(f"Значения элементов в этих позициях:  {list[position[0]]} и {list[position[1]]}")
    print(f"Их сумма: {sum}")
else:
    print("ERROR! Позиции вне диапазона значений.")