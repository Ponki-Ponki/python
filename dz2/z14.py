# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


num = input("Введите число: ")

sum = 0
for i in range(0,len(num)):
    if num[i] != "," and num[i]!= "-" and num[i]!= ".":
        sum += int(num[i])

print(f"Сумма чисел из числа {num} -> {sum}")