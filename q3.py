import random

# Update this dictionary with questions and answers:
flashcards = {
    "spanish" : "inglish",
    "zorro" : "fox",
    "gato" : "cat"
}

# Get a list of keys (questions) from the dictionary
keys = list(flashcards.keys())
values = list(flashcards.values())

#print(keys)

# Randomly sample one question
#print(random.choice(keys))

# Use the `input` function to ask the user the question and get their response
memory = input(f"what is {random.choice(keys)} in inglish?")

# Use the question as a key to look up the answer in the dicitonary
for value in values:
    if memory == value:
        print("correct!")
        break
    else:
        print(f"not quite! the awnser was {value}!")
        break

# Check if the response is the same as the answer, and give the user
# feedback based on whether their response was correct or incorrect
#### YOUR CODE HERE