import random
import module_file_editing as file

l_n = file.file_read('name_l.txt')
f_n = file.file_read('name_f.txt')
list_lesson = file.file_read('lesson.txt')
list_name = zip(l_n, f_n)

def create_student(data):
    global list_name
    for item in list_name:
        temp = item[0].strip()+' '+item[1].strip()
        data[temp] = {}
        data[temp][list_lesson[random.randint(0, 34)].strip()] = \
            [random.randint(1, 5) for i in range(5)]
    return data
