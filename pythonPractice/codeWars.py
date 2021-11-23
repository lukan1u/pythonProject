def disemvowel(string):
    return print("".join(c for c in string if c.lower() not in "aeiou"))
    # join means what character will be replaced
    # it means search each element in string for the elements that aren't vowels and replace them

disemvowel("Hello everybody my name is lukasssss")