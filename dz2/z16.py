# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input("Введите число: "))
answer = {}
sum = 0
for i in range(1, n+1):
    sum += round((1 + 1/i)**i, 2)
    answer[i] = round((1 + 1/i)**i, 2)

print(f"Для n={n}  {answer}")
print(round(sum, 3))