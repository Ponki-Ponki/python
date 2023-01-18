# Напишите программу, удаляющую из текста все слова, 
# содержащие ""абв"".(Задание из семинара)


text = "собака стабвол абв кот абв стул абв цифабвра"

text_split = text.split(" ")
new_text = []
for i in text_split:
    if i.find("абв") == -1:
        new_text.append(i)
        
text = " ".join(new_text)
print(text)