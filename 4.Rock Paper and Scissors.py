#code to make simple rock paper ans scissors game to play with computer
import random
user=" "
system=" "

while(1):
    def rsp():
        user = input("Choose your choice (r) for Rock,(p) for Paper and (s) for scissors :")
        system = random.choice(['r', 's', 'p'])
        game_start(user,system)


    def game_start(user,system):
        if user == system:
            print("It is a Tie")
        elif (user =='r' and system == 's') or (user =='s' and system == 'p') or (user == 'p' and system == 'r'):
            print("yaay ,you win")
        else:
            print("you lost try again")



    rsp()

