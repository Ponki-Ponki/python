import mod_add_student as add_student
import mod_add_lesson as add_less
import mod_viev as v
import mod_add_less_eval as eval
import create_base_names as create

def working_base():        
	data = {}
	while True:
		vol = v.menu()
		if vol == 0:
			data = create.create_student(data)
		if vol == 1:        
			data = add_student.add(data)
		if vol == 2:
			data = add_less.add_lesson(data)
		if vol == 3:
			eval.add_eval(data)
		if vol == 4:
			v.viev_students(data)
		if vol == 5:
			v.viev_stud_eval(data)
		if vol == 6:
			exit()
		if vol == 7:
			v.average_grade(data)
		if vol == 9:
			data.clear()
		if 1>vol>6:
			print('Error input')
    