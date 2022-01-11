def arrey_diff(a, b):
    listo = []
    for element1, element2 in zip(a,b):
        listo.append(element1 - element2)
    return print(listo)

listo1 = [1,2,3,4,5,6,7,8,9]
listo2 = [5,4,3,2,1,2,3,4]
arrey_diff(listo1, listo2)
