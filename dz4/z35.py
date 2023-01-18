# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import file

file1 = "file_z35.1.txt"
file2 = "file_z35.2.txt"

list1 = file.file_read(file1)
list2 = file.file_read(file2)


def sia(i,list):   #splitting into arguments / дробление на аргументы
    str = list[i].split(" + ")
    str[-1] = str[-1].replace(" = 0","")
    return str

def some_di(list):
    some_dict = {}
    for el in list:
        if '*' in el:
            some_dict[el[el.index('*'):]] = el[:el.index('*')]
        else:
            some_dict[''] = el
    return some_dict


def create_new_mch(list1,list2):
    new_result_list = []
    for i in range(len(list1)):
        new_list =[]
        file1 = sia(i,list1)
        book1 = some_di(file1)
        file2 = sia(i,list2)
        book2 = some_di(file2)
        for i in book1:
            if i in book2:
                new_list.append(str(int(book1[i]) + int(book2[i])) + i)
            else:
                new_list.append(book1[i] + i)
        for i in book2:
            if i not in book1:
                new_list.append(book2[i] + i)
        new_result_list.append(new_list)
    return new_result_list

result_list = create_new_mch(list1,list2)
path = "result.txt"

for i in range(len(result_list)):
    str = " + ".join(result_list[i]) + " = 0\n"
    file.file_write(path,str)
