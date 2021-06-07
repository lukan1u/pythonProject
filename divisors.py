def divisors(num):
    # saves range in x
    x = range(1, num)
    return print([elements for elements in x if num % elements == 0])

divisors(100)
