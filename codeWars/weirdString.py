def accum(s):
    newstring = ""
    for i in s:
        newstring = s.index(i) * i
        return newstring
        

print(accum("abcde"))
