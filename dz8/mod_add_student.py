
def input_name():
    print('Please input First name and Last name')
    return input()

def add(data):
    name = input_name()
    if len(data) == 0:
        data[name] = {}
    else:
        list1 = list(data.values())
        for i in list1[0]:
            list1[0][i] = []
        data[name] = list1[0]
    return data
