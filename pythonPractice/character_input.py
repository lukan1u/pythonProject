import datetime

def age_calculator(name, age, copy):
    currentDate = datetime.datetime.now()
    currentDate = currentDate.strftime("%Y")
    year = int(currentDate) - age + 100

    sentence = str("Hello {}, did you know that in {} you will turn up 100 years old?\n".format(name, year))
    return print(copy * sentence)


age_calculator(str(input("Enter your name:\n>>> ")),
                int(input("Enter your age:\n>>> ")),
                int(input("How many time would you like to print message?\n>>> ")))
