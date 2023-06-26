import random
def rockPaperScissor():

    turn = int(input("How many times do you want to play? "))
    option = ["rock","paper","scissor"]
    userPoint = 0
    botPoint = 0

    while turn !=userPoint and turn !=botPoint:
        userTurn = input("choose rock or paper or scissor: ").lower()
        botTurn = random.choice(option)
        
        while userTurn not in option:
            userTurn = input("You must select a rock or paper or scissor. Try again: ").lower()

        print("Computer selected: ", botTurn)
        print("You selected: ", userTurn)
        
        if(userTurn == "rock" and botTurn == "paper") or (userTurn == "scissor" and botTurn == "rock") or (userTurn == "paper" and botTurn == "scissor"):
            print("you lost!!!")
            botPoint += 1
        elif userTurn == botTurn:
            print("Draw!!!")
        else:
            print("You won!!!")
            userPoint += 1   

        print("Your point is: ",userPoint)
        print("Computer point is: ",botPoint)

                        
rockPaperScissor()    