# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input()
if 10**-1 >= float(d) and 10**-10 <= float(d):
    print(round(math.pi, len(d)-2))