import module_load_base as load
import module_add_data as add_data
import module_sort_base as sort
import module_output as output
import module_unloading_base as unload

def working_base():
    works = True        
    # path = load.name_base()
    path = 'base.csv'
    data = load.load_data(path)
    while works:
        print("Actions:\n 1. Add data \n 2. Sort data base \n 3. Import base \n 4. Import first name and last name \n 5. Exit")
        vol = int(input('Please select action '))
        if vol == 1:        
            data = add_data.add(data)
        if vol == 2:
            flag = sort.flag()
            data = sort.sort_base(data, flag)
        if vol == 3:
            output.output(data)
        if vol == 4:
            output.output_name(data)
        if vol == 5:
            works = False
    unload.write_data(path, data)