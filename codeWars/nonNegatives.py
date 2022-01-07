def filter_list(l):
    return [i for i in l if type(i) == int and i > 0]

filter_list([1, 2, 3, "abc"])
