import mod_add_student as ad_s
import mod_add_lesson as ad_l
import mod_viev as v

def add_eval(data):
	if len(data) == 0:
		v.err_log
	else:
		name_s = ad_s.input_name()
		for studen in data:
			if name_s == studen:
				print("studen found")
				for item in data[studen]:
					print(f"{item}: {data[studen][item]}")
				name_l = ad_l.name_less()
				for lesson in data[studen]:
					if name_l == lesson:
						print("lesson found")
						data[name_s][name_l].append(int(input("Please input evalation: ")))
						break
	return data