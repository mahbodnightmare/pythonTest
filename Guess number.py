import random 
def guessNumber():
    number = int(random.randint(1,50))
    userGuess = int(input("Please enter your guess between 1 and 50: "))

    decrement = 0

    while userGuess == number or userGuess > number or userGuess < number:
        if userGuess == number:
            print("You guessed it right!")
            break
        elif userGuess > number:
            userGuess = int(input("Too high,guess again: "))
        else:
            userGuess = int(input("Too low,guess again: ")) 

        decrement += 1  


guessNumber()


