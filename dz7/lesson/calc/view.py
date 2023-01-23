def view_data(data, title):
    print(f'{title} = {str(data)}')
    
def error(type_err = 'input'):
    print(f'Error {type_err}')
    exit()

def get_int_or_complex():
    print('Please select integer or complex operations (1 - integer; 2 - complex)')
    value = int(input())
    if value == 1:
        return True
    elif value == 2:
        return False
    else: 
        error()
        
def get_value():
    try:
        return int(input('value = '))
    except:
        error()
        
def get_value_complex():
    try:    
        value = input('value(example "1+1j") = ').replace(" ", "")
        return complex(value)
    except:
        error()

def get_value_operator(bool):
    if bool:
        print('Please input opretor(*,-,+,/,//,%)')
    else: print('Please input opretor(*,-,+,/)')
    return input('Operator: ')