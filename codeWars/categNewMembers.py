def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data] # the elements NAMES relate to both objects inside of bigger element

# def openOrSenior(data):
#     res = []
#     for i in data:
#       if i[0] >= 55 and i[1] > 7:
#         res.append("Senior")
#       else:
#         res.append("Open")
#     return res 
    