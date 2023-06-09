
list_special = ["@", "!"]
def loda(s):
    if s[0] in list_special:
            print(True)
    else: 
        if len(s) != 1:  
            loda(s[1:])
        else: 
            print(False)

loda("mathematics!")