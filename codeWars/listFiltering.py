def filter_list(l):
    l = [x for x in l if not isinstance(x, str)] #isisnstance is asking for datatype
    return l

print(filter_list([1,'a','b',0,15]))