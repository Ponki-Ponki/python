# Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input())
b = int(input())

def degree_of_number(a,b):
	if b>0:
		return a*degree_of_number(a,b-1)
	elif b == 0: return 1
	else: return 1/(a*degree_of_number(a,-b-1))

print(f"A = {a}; B = {b} -> {degree_of_number(a,b)}")