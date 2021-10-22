def diamond(n):
    # Make some diamonds!
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n/2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
            diamond += "\n"
        return diamond
    else:
        return None
diamond(5)


# expetced output: "  *\n ***\n*****\n ***\n  *\n"