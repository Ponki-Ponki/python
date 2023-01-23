x = 0
y = 0

def init(a, b):
    global x
    global y
    x = a
    y = b
    
operators = { '+': lambda x,y: x+y, 
            '*': lambda x,y: x*y, 
            '-': lambda x,y: x-y,
            '/': lambda x,y: x/y 
            }

def do_it(value): 
    try:
        return operators.get(value)(x,y)
    except:
        print('Error input operator')
        exit()