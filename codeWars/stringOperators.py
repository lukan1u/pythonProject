def arithmetic(a, b, operator):
    a = str(a)
    b = str(b)
    operator = operator.replace("add","+")
    operator = operator.replace("subtract","-")
    operator = operator.replace("multiply","*")
    operator = operator.replace("divide","/")

    value = (a + operator + b)
    return eval(value)

print(arithmetic(10,10,"add"))

# return {
#         'add': a + b,
#         'subtract': a - b,
#         'multiply': a * b,
#         'divide': a / b,
#     }[operator]