import module_html_creater as html

def console_print(data,flag):
    if flag == 0:
        for item in data:
            item = item.split(',')
            print((f"{item[0]}  {item[1]} {item[2]} {item[3]}  {item[4]}"))
    if flag == 1:
        for item in data:
            print(f"{item[0]} {item[1]}")
    
def output(data):
    print('Output print in console(1) or html-file(2)?')
    flag = ''
    while flag != 1 or flag != 2:
        flag = int(input('Please flag (1 or 2): '))
        if flag == 1 or flag == 2:
            break
    if flag == 1:
        console_print(data,0)
    else: html.create_full(data)

def output_name(data):
    first_name =[]
    last_name = []
    for item in data[1:]:
        first_name.append(item.split(',')[1])
        last_name.append(item.split(',')[2])
    result = zip(first_name,last_name)
    print('Output print in console(1) or html-file(2)?')
    flag = ''
    while flag != 1 or flag != 2:
        flag = int(input('Please flag (1 or 2): '))
        if flag == 1 or flag == 2:
            break
    if flag == 1:
        console_print(result,1)
    else: html.create(result)
