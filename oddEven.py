def oddOrEven(number, checker):
    if number % 4 == 0:
            print("your number divides evenly by 4")
    else:
        print("your number dosnen't divides evenly by 4")
        
    if number % checker == 0:
        print("your number divides evenly")
    else:
        print("your number is odd")

oddOrEven(int(input("Enter your number: ")),
        int(input("Enter your checker: ")))