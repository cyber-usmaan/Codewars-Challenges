'''

Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.

'''

def disemvowel1(string_):
    vowel = "aeiouAEIOU"  #string of vowels to match and compare
    for char in vowel: string_ = string_.replace(char, "")  #match vowel from string and remove with replace function
    return string_

# Revised to make it shorter
def disemvowel(string_):
    for char in "aeiouAEIOU": string_ = string_.replace(char, "")
    return string_
