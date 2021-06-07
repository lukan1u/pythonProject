def palindrome(word):

    word = word.lower()

    if word == word[::-1]:
        print("your word is a palindrome")
    else:
        print("your word is NOT a palindrome")

palindrome(str(input("Type word to check if it is palindrome:\n>>> ")))


