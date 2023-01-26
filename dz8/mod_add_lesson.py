import mod_viev as v

def name_less():
    return input('Please input name lesson: ')

def add_lesson(data):
    if len(data) == 0:
        v.err_log()
    else:
        lesson = name_less()
        for key in data:
            data[key][lesson] = []
    return data