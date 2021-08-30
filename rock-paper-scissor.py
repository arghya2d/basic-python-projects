import random

print("Lets play Rock Paper Scissors...Best of three turn wins!\n")
username = input("Enter your name: \n")


def system_response():
    system_choices = ["R", "P", "S"]
    system_choice = random.choice(system_choices)
    return system_choice


def decision(user_choice, system_choice, username):
    if user_choice == "R" and system_choice == "P":
        return "user"
    if user_choice == "R" and system_choice == "S":
        return "user"
    if user_choice == "R" and system_choice == "R":
        return "draw"
    if user_choice == "P" and system_choice == "R":
        return "user"
    if user_choice == "P" and system_choice == "S":
        return "system"
    if user_choice == "P" and system_choice == "P":
        return "draw"
    if user_choice == "S" and system_choice == "R":
        return "system"
    if user_choice == "S" and system_choice == "S":
        return "draw"
    if user_choice == "S" and system_choice == "P":
        return "user"


count = 1
user_win = 0
system_win = 0
while count <= 3:
    user_choice = input("Enter your choice: R = Rock P = Paper S = Scissor: \n")
    if user_choice not in ["R", "P", "S"]:
        while user_choice not in ["R", "P", "S"]:
            print("Wrong choice. Try again..")
            user_choice = input("Enter your choice: R = Rock P = Paper S = Scissor: \n")
    system_choice = system_response()
    print(username + " Chose " + user_choice + "\n" + "System responded with " + system_choice)
    game_decision = decision(user_choice, system_choice, username)
    if game_decision == "user":
        user_win = user_win + 1
        print(username, user_win, "system", system_win)
    if game_decision == "system":
        system_win = system_win + 1
        print(username, user_win, "system", system_win)
    if game_decision == "draw":
        print(username, user_win, "system", system_win)
    count = count + 1

if user_win > system_win:
    print("Congratulation!! You win!")
elif system_win > user_win:
    print("system wins...")
else:
    print("Draw!")



