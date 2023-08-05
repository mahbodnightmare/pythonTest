import random
import nltk

# Download the words corpus (only required once)
nltk.download('words')

# Get a list of English words from the nltk words corpus
nltk_words = nltk.corpus.words.words()

used_words = set()

while True:
    # Filter out non-lowercase words and select 12 random words
    available_words = [word.lower() for word in nltk_words if word.lower() not in used_words]
    
    if len(available_words) < 12:
        print("Not enough unique words left. Restarting the list.")
        used_words = set()
        continue
    
    random_words = random.sample(available_words, 12)

    print("Random words:", random_words)

    # Add the newly generated words to the used_words set
    used_words.update(random_words)

    # Ask the user if they want more words
    user_input = input("Do you want more words? (yes/no): ").strip().lower()

    while user_input not in ['yes', 'no']:
        user_input = input("Please write a correct answer (yes/no): ").strip().lower()

    if user_input == 'no':
        print("Ok!")
        break