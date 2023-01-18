# Реализуйте     алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E


from itertools import groupby

a = "AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE"  # /input()

el = [list(g) for k, g in groupby(a)]
str= ""
for i in el:
    str = str + f"{len(i)}{i[0]}"    
print(str)
