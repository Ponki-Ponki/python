# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10



def convert_to_01(number: int):
	new_number = []
	while number != 0:
		new_number.append(str(round(number%2, 3)))
		number = number // 2
	new_number.reverse()
	print("".join(new_number))

n = int(input("Input value "))
print(f"{n}:  ", end="")
convert_to_01(n)

for i in range(10 , 100, 5):
    print(f"{i}:  ", end="")
    convert_to_01(i)