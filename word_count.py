# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:  # Iterate through all the words in the line.
                # Place lowercased version of words.
                if ht.contains_key(w.lower()):  # If the word is in the hashmap.
                    ht.put(w.lower(), ht.get(w.lower()) + 1)  # Update the word count by 1.
                else:  # If the word does not exist in the hashmap.
                    ht.put(w.lower(), 1)  # Place the key in the map with the value of 1.
                    keys.add(w.lower())  # Add the new keys into the keys set.

    list_of_occurences = []  # Create an empty list to hold the tuples of keys and values.
    for key in keys:  # Iterate through all the keys.
        list_of_occurences.append((key, ht.get(key)))  # Add the key and value tuple into the list.

    # Source to help me find a way to implement this:
    # stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value

    # We use lambda here to sort the list of tuples by its second value.
    # The sorting is also reversed to make it in descending order.
    sorted_list = sorted(list_of_occurences, key=lambda x : x[1], reverse=True)
    return sorted_list[:number]  # Using list slice, return the top numbers of the list depending on what the user inputs

# print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE