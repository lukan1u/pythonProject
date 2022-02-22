def alphabet_positon(text):
    text = text.lower()
    dicto = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6, 
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }

    string = ""
    for elements in text:
        # kets are the strigns
        if elements in dicto.keys():
            # get gets the value of a key
            x = dicto.get(elements)
            if x == "":
                x.replace("", "")
            string = string +  " " + str(x)
        else:
            text.replace(elements, "")


    return string[1:]

a = "Hello Everybody"



# ord returns number that represent specific character
# isaplha checks if the letter is in alphabet
# 96 because the ord of c for letter "h" is 104 so if we minus 96 it will become 8
"""
' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""

alphabet_positon(a)
