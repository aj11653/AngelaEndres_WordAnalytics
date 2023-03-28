# This function returns the entirety of Dracula as a string and removes any character that is not a digit, letter, or space
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")
  
# Load the book
draculaText = readBook()
# Convert all words to lower case
draculaText = draculaText.lower()
# Convert the text into a list of words
draculaWords = draculaText.split()

# Create a dictionary for words in Dracula
wordBank = {}

# Go through each word...
for word in draculaWords:
  # Account for capitalization differences
  word = word.lower()
  # Is it already in the dictionary?
  if word in wordBank:
    # If so, increment it's count
    wordBank[word] += 1
  # If not, create the pair and set it's initial count to 1
  else:
    wordBank[word] = 1

# Create a buffer that represents the current most common word
mostOccuring = "dracula"
# Create a for loop to find the most occuring word in Dracula
for word in wordBank:
  # See if the "challenger" better meets the criteria (occurs more) than the current "king"
  if(wordBank[word] > wordBank[mostOccuring]):
    #If so, the "challenger" is now the "king"
    mostOccuring = word

# Displays how many unique four-letter words are in the book
# Create a list for unique words
uniqueWords = []
# Go through all words in Dracula's dictionary
for key in wordBank:
  # If the current word is not already in our list of unique words...
  if (wordBank[key] not in uniqueWords):
    # Add it to the list
    uniqueWords.append(key)
# Create variable for four letter words
fourLetterWords = 0
# Go through all the unique words
for word in uniqueWords:
  # If the word is four letters long...
  if (len(word) == 4):
    # Add one to the count
    fourLetterWords += 1

# Display results
print("=== RESULTS ===")
print()
# Displays most found word and how many times it appears
print(f"'{mostOccuring}' is the word that appears the most throughout the text for a total of {wordBank[mostOccuring]} times.")
# Displays number of unique four letter words
print()
print(f"There are {fourLetterWords} words that are four letters long.")
# Prints every word that shows up more than 500 times, and how many times that word shows up throughout the book
print()
print("I noticed that these words show up more than 500 times: ")
# Look through the dictionary
for pair in wordBank:
  # If it shows up more than 500 times...
  if wordBank[pair] > 500:
    # Print the word and its count
    print(f"{pair} - {wordBank[pair]}")