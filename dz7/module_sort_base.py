
def flag():
    print('Please select sort id(1) or first name(2)')
    fl = int(input())
    if fl == 1 or fl == 2:
        if fl == 1:
            fl = 'id'
        else: fl = 'first name'
        return fl
    else:
        print('Error select')
        flag()


def sort_base(data,flag):
    if flag == 'id':
        data = data[:1] + sorted(data[1:], key = lambda x: int(x.split(',')[0]))
    elif flag == 'first name':
        data =data[:1] + sorted(data[1:], key = lambda x: x.split(',')[1])
    return data