# input example =  [{name: Brat}, {name: Bee}, {name: Josh}] it's scaleable
# output exmaple = "Brat, Josh & Bee"

def namelist(names):
    lenght = len(names)
    allNames = ""
    counter = 0
    while lenght > counter:

        if names == []:
            return ""

        elif lenght == 1:
            return "{}".format(names[counter]["name"])
        
        elif lenght == 2:
            return "{} & {}".format(names[counter]["name"],names[counter + 1]["name"])

        else:
            allNames += names[counter]["name"]
            counter = counter + 1
            if counter == lenght - 1:
                allNames += " & "
            else:
                allNames += ", "
        
    return allNames[0:-2]

print(namelist([{'name': 'Bart'},{'name': 'Bsart'},{'name': 'Badsart'},{'name': 'Baasdfasrt'},{'name': 'Bardsafdasfast'}]))

# better solution
# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''
