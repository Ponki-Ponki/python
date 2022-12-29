# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import file


def create_x(k):
    result_str = []
    if k == 0:
        result = "error create"
        return result
    else:
        for i in range(k, -1, -1):
            a = random.randint(0, 100)
            if a > 0:
                if i == 1:
                    result_str.append(str(a) + '*x')
                elif i == 0:
                    result_str.append(str(a))
                else:
                    result_str.append(str(a) + '*x**' + str(i))
    return " + ".join(result_str)+ " = 0\n"


k = int(input("Введите степень: "))
path = "file_z33.txt"
equation = create_x(k)
print(equation)
print(file.file_write(path, equation))