def divisors(n):
    numList = range(1, n)
    actualList = []
    for elements in numList:
        if n % elements == 0:
            actualList.append(elements)
    return len(actualList)

print(divisors(2000))