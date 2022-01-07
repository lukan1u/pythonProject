def namelist(names):
    # how to access specific item within list of dictionaries
    x = names[1]["name"] 
    return x

print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))

a = "abc"
print(a[1])