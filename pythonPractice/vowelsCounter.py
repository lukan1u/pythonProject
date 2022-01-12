def get_count(sentence):
    vowels = ["a","e", "i", "o", "u"]
    final = [elements for elements in sentence if elements in vowels]
    return print(len(final))

get_count("aeiou")
    