from os import system
import time

def clear():
    return system("clear")


def prime_checker(x):
    if x % 2 == 0:
        print("➔➔ your number is dividable by 2")
    elif x % 2 != 0:
        print("➔➔ your number is not a prime number")

    time.sleep(3)
    clear()

prime_checker(int(input("Enter your number to check wheather it's prime\n>>> ")))
