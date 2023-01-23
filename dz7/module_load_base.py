import module_file_editing as file

def name_base():
    path = input("Please enter the name of the database file ('base.csv')")
    if ".csv" or ".txt" in path:
        return path
    else:
        print("Error name")
        return 0        

def read_file(path):
    data = file.file_read(path)
    return data

def load_data(path):
    try:
        return read_file(path)
    except:
        print("Error load base, create new base")
        file.file_write(path, str = "id,First Name,Last Name,Telephone number,Comment\n")
        return read_file(path)
