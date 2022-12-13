#create a random number and guess the number


import random

range = int(input("Enter the range for the secret number :"))

def guess():
    secret_number=random.randint(1,range)
    x=int(input(f"Enter your guess between 1 and {range} :"))
    while x!=secret_number:
        print("Your guess is incorrrect.please try again")
        if x > secret_number:
            print("Your guess too high.TRy AGAIAN")
        elif x < secret_number:
            print("Your guess is too low.TRY AGAIAN")
        x = int(input("Enter your guess :"))
    print(f"Your guess is corrrect.The secret number is {x}")
guess()


