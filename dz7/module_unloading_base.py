import module_file_editing as file

def write_data(path, data):
    result = ''
    for item in data:
        result += item
    try:
        file.file_write(path, result)
    except:
        print("Error write")

