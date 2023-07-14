import random

class MyFunction:
    def __init__(self):
        self.number = None
        self.decrement = 0

    def play_game(self):
        self.number = random.randint(1, 50)
        user_guess = int(input("Please enter your guess between 1 and 50: "))

        while True:
            if user_guess == self.number:
                print("You guessed it right!")
                break
            elif user_guess > self.number:
                print("Too high, guess again.")
            else:
                print("Too low, guess again.")

            self.decrement += 1
            user_guess = int(input("Please enter your guess between 1 and 50: "))

def palindrome(userWord):
    letter = len(userWord) - 1
    reversedText = ""

    while letter >= 0:
        reversedText = reversedText + userWord[letter]
        letter -= 1

    if reversedText.lower() == userWord.lower():
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome") 

def reverse(text):
    i = len(text) - 1
    reversedText = ""
    
    while i >= 0:
        reversedText = reversedText + text[i]
        i -= 1
    print(reversedText)

def rockPaperScissor():
    turn = int(input("How many times do you want to play? "))
    option = ["rock","paper","scissor"]
    userPoint = 0
    botPoint = 0

    while turn != userPoint and turn != botPoint:
        userTurn = input("Choose rock, paper, or scissor: ").lower()
        botTurn = random.choice(option)
        
        while userTurn not in option:
            userTurn = input("You must select rock, paper, or scissor. Try again: ").lower()

        print("Computer selected:", botTurn)
        print("You selected:", userTurn)
        
        if (userTurn == "rock" and botTurn == "paper") or (userTurn == "scissor" and botTurn == "rock") or (userTurn == "paper" and botTurn == "scissor"):
            print("You lost!")
            botPoint += 1
        elif userTurn == botTurn:
            print("Draw!")
        else:
            print("You won!")
            userPoint += 1   

        print("Your point is:", userPoint)
        print("Computer point is:", botPoint)

game = MyFunction()
game.play_game()

reverse(input("Please enter your word to reverse: "))

palindrome(input("Please enter a word: "))

rockPaperScissor()
