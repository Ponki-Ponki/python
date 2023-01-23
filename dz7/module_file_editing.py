import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def file_read(path):
    data = open(os.path.join(__location__, path), 'r')
    a = [line for line in data]
    data.close()    
    return a

def file_write(path, str):
    data = open(os.path.join(__location__, path), 'w')
    data.write(str)
    data.close()    
    return "Recorded!"