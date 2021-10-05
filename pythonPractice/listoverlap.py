from random import randint

def randomiser(listLength, listNumbers):
    a = []
    b = []

    for elements in range(randint(1, listLength)): # random list lenght
        a.append(randint(1, listNumbers)) # random numbers
        b.append(randint(1, listNumbers))

    c = {elements for elements in a if elements in b} # set without duplicates
    return sorted(c) # pretty list

print("hello".format())

print(randomiser(30, 40))
# hello world 