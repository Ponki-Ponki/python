# # Реализуйте алгоритм перемешивания списка.

import random

list = [1,2,3,4,5,6,7,8,9]

# random.shuffle(list)
# print(list)


new_list = []

print(list)
for i in range(len(list)):
    if len(list) > 0:
        ran = random.randint(0, len(list)-1)
        new_list.append(list[ran])
        list.pop(ran)
    
print(new_list)