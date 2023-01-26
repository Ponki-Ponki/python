import mod_add_student as ad_s

def err_log():
    print("\nLog is empty!\n")

def viev_students(data):
    i = 1
    if len(data) == 0:
        err_log()
    for item in data:
        print(f"Ученик {i}: {item}")
        i+=1

def viev_stud_eval(data):
    if len(data) == 0:
        err_log()
    else:
        name = ad_s.input_name()
        print("Оценки ученика")
        for item in data[name]:
            print(f"{item}: {data[name][item]}")
        return name

def average_grade(data):
    name = viev_stud_eval(data)
    less = input('Please input lesson: ')
    eval =  data[name][less]
    if len(eval)>0:
        print(f"{less} средняя оценка: {sum(eval)/len(eval)}")
    else: print("Оценок нет")
            
def menu():
        print("\nActions:\n 1. Add student\n 2. Add subject\n 3. Add a student's grade on a lesson\n 4. Show a list of students\n 5. Showing a student's grade sheet\n 0. Autocomplete \n 7. Average grade per subject\n 6. Exit \n")
        return int(input('Please select action '))