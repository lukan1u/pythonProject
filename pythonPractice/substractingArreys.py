def arrey_diff(a, b):
    listo = []
    for element1 in a:
        for element2 in b:
            listo.append(element1 - element2)
        return print(listo)


listo1 = [300, 100]
listo2 = [9,8,7,5,5,4,3,2,1]
arrey_diff(listo1, listo1)
