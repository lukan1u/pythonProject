print("hello world")
try:
     sa = open("hello.txt")
except FileNotFoundError:
    sa = open("hello.txt", "w")

sa.write("FirstLine")
sa.close()
a = [1,2, 3,4,5]