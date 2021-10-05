a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def listo(list, less):
    a = []
    for elements in list:
        if elements < less:
            a.append(elements)
    return print(a)

listo(a, int(input("Enter number: ")))
