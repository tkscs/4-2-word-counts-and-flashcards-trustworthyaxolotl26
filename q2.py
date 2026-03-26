"""
INSTRUCTIONS:
The code below has a lot of repetition. Use a dictionary and a for loop to 
make the code more compact.
"""

def pad_word_count(essay):
    """
    Add more words to an essay by replacing any contractions with two separate
    words.

    Parameters:
    essay (str): the original essay

    Returns:
    str: a new essay with more words
    """
    # Initialize new essay to match the original.
    # We will update it and re-assign this variable later.
    new_essay = essay

    #### START REPLACING CODE HERE
    newer_essay = {"n't": " not", "'s": " is","'re": " are", "'ve": " have" }

    keys = list(newer_essay.keys())
    values = list(newer_essay.values())
    for key in keys:
      value = newer_essay[key]
      new_essay = new_essay.replace(key, value)

    #### STOP REPLACING CODE HERE

    return new_essay

# Here's the function call.
# Don't change this.
print(pad_word_count(
  """
  Cats are cute.
  They've been pets for thousands of years.
  They're playful and cuddly, but they don't need as much attention as dogs.
  It's clear that they're silly, and they love knocking things over.
  It isn't possible to see a cat and not want to cuddle it.
  That's all I have to say about cats."""
))