# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

def search_list(list_item):
    answer = []
    leg = [0 for i in range(len(list_item))]
    for i in range(0,len(list_item)):
        if list_item[i] in list_item[i:]:
            leg[list_item[i]-1] += 1
    for i in range(0,len(leg)):
        if leg[list_item[i]-1] == 1:
            answer.append(list_item[i])
    return answer

# a = [1,2,3,4,4,6,1,1,9]
a = [random.randint(0,9) for i in range(10)]
print(a)
print(search_list(a))