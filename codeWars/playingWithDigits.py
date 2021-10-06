def dig_pow(n, p):
    #splits int into seperate numbers
    na = [int(x) for x in str(n)]
    c = []
    for x in na:
        calculation = x ** p
        c.append(calculation)
        p = p + 1  
    
    if sum(c) % n == 0:
        return int(sum(c) / n)
    else:
        return -1

print(dig_pow(46288, 3))

# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)): # i for item c for counter
#      s += pow(int(c),p+i)  # here is sum and **
#   return s/n if s%n==0 else -1 # smart way of if statemtment
