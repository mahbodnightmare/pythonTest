def revese(text):

    i = len(text) - 1

    reversedText = ""
    
    while i >= 0:

        reversedText = reversedText + text[i] 
        i -= 1
        if len(reversedText) == len(text):
            print(reversedText) 
           

revese(input("Please enter your word to revese: "))