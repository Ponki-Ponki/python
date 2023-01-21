# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше
# заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]


list_num = [-5, 9, 0, 3, -1, -2, 1, 4, -2,
            10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 5
max = 15

# n = int(input("length list_mumber"))
# list_num = [int(input("list_number ")) for i in range(n) ]
# min = int(input("min"))
# max = int(input("max"))

result = []
for ind,val in enumerate(list_num):
    if val>min and val<max:
        result.append(ind)
print(list_num)
print(result)