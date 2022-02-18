def invert(lst):
    return [abs(i) if i < 0 else -abs(i) for i in lst ]


# minus and minus gives plus 
lol = [-1,-2,-3]
co = []
for x in lol:
    co.append(-x)