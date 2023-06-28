def palindrome(userWord):
    letter = len(userWord) - 1
    reversedText = ""

    while letter >= 0:
        reversedText = reversedText + userWord[letter]
        letter -= 1
        
    
    if reversedText == userWord:
        print("The word is a palindrome")
    else:
        print("The word is not a palindrome")    

          

palindrome(input("Please enter your word to check is a palindrome or not:"))        