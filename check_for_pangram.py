'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

from string import ascii_lowercase #lowercase alphabets from a to z

def is_pangram(st):
    return all(char in st.lower() for char in ascii_lowercase) # check if all char from st in lowercase are in ascii_lower
