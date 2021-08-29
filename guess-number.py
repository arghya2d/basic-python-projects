import random
print("Welcome to the Guessing Game\n" + "Guess a number\n" + "If the no equals the no chosen by the system you win\n" + "You get 3 chances and 2 hints!!\n")
count = 1
while count <= 3:
    RandomNum = random.randint(1, 100)
    RandomNumString = str(RandomNum)
    digit = random.choice(RandomNumString)
    bar = range(2, RandomNum - 1)
    flag = 0
    for foo in bar:
        if RandomNum % foo == 0:
            flag = 1
            break
    print("----- HINTS -----")
    if flag == 1:
        print("Number is not a prime")
    else:
        print("Number is prime")
    print("One of the digits of the number is", digit)
    print("-----------------\n")

    count = count + 1

    UserNum = int(input("Guess a number: "))
    if UserNum == RandomNum:
        print("Congratulations!! Number is", UserNum)
        print("\n")
    else:
        print("Sorry.. Number is", RandomNum)
        print("\n")
    if count > 3:
        print("Thanks for Playing..")
