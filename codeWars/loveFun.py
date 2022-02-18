def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False

# logic True if 0 and False if not
# (flower1+flower2)%2