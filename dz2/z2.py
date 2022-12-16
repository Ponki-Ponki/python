# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Введите число: "))
result = []
for i in range(1,num+1):
    if i == 1:
        result.append(i)
    else:
        result.append(i*result[i-2])

print(f"Пусть N = {num}, тогда  {result}")