# Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите день недели: "))
if a<=5 and a>=1:
    print(f"{a} -> нет")
elif a==6 or a==7:
    print(f"{a} -> да")
elif a>7 or a<1:
    print(f"{a} -> не правильный день недели")