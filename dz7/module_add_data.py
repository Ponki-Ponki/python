import module_unloading_base as write

def create_str(value):
    print("Add data")
    id = ''
    id = str(int(value.split(',')[0]) + 1)
    first_name = input("Please input first name: ")
    last_name = input("Please input last name: ")
    tel = input("Please input telephone number: ")
    comment = input("Please input comment: ") + '\n'
    if first_name == '':
        first_name = '-'
    if last_name == '':
        last_name = '-'
    if tel == '':
        tel = '-'
    if comment == '':
        comment = '-\n'
    item = [id,first_name,last_name,tel,comment]
    print(item)
    item = ','.join(item)
    print(item)
    return item
    
    
    
def add(data):
    item = create_str(data[-1])
    data.append(item)
    return data
    