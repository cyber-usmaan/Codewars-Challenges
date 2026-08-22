'''
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
'''

def find_short(s):
    words = s.split()  #split line in list of words
    l = len(words[0])  #set shortest length to the first letter of word
    
    for word in words:
        n = len(word)  #get lenght of each word in list
        if n < l:      #compare for short length
            l = n      #l has sortest length of word
            
    return l # l: shortest word length

'''
def find_short(s):
    return min(len(x) for x in s.split())
'''
