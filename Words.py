import random
import nltk

# Download the words corpus (only required once)
nltk.download('words')

# Get a list of English words from the nltk words corpus
nltk_words = nltk.corpus.words.words()

# Filter out non-lowercase words and select 12 random words
random_words = random.sample([word.lower() for word in nltk_words], 12)

print(random_words)

user_input = input("Do you more words? (y/n): ")