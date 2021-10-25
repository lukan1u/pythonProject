def paperwork(n, m):
    if not n or m <= 0:  # it cannot be equal to 0 that's why it's not
        return 0
    elif n <= 0:
        return 0
    else:
        return n * m


print(paperwork(-5, 5))

# better solution:
# def paperwork(n, m):
#    return n * m if n > 0 and m > 0 else 0