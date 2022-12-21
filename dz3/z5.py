# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


    
def fibon(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibon(n-1) + fibon(n-2)


n = int(input('Введите длину ряда: '))

def fibon_and_not_fibon(n):
    result = [0]
    for i in range(1, n+1):
        result.append(fibon(i))
        result.insert(0, ((-1)**(i+1))*fibon(i))
    return result

print(fibon_and_not_fibon(n))