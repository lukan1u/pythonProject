mydict = {
    83: 80
}

lol = "helpS me man!"
print(lol.translate(mydict))

print(lol.translate(str.maketrans("hel", "123")))