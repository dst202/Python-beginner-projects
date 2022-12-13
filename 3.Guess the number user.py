#code to make the computer play our guessing game

import random
def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        guess = random.randint(low,high)
        feedback = input(f"system guess is  {guess} false.please give the feedback :").lower()
        if feedback =="l":
            low = guess + 1
        elif feedback == "h":
            high = guess - 1


    print(f"systems guess is correct {guess}")

computer_guess(1000)

