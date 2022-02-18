
def open_or_senior(data):
    listo = ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]
    return listo


attmept([(45, 12),(55,21),(19, -2),(104, 20)])
# open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])
