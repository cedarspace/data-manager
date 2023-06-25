string1 = "/Users/cedarspace/Documents/GitHub/data-manager/data_manager/cli.py"

new_list = list(string1.split("/"))


def name_puller(name): 
    los = list(name.split("/"))
    reverse_los = list(reversed(los))
    file_name = reverse_los[0]
    los2 = list(reversed(list(file_name.split("."))))
    file_name = los2[1]
    print(file_name)
def file_type_puller(file_name):
    los2 = list(reversed(list(file_name.split("."))))
    file_type = "." + los2[0]
    print(file_type)

    return file_name

name_puller(string1)