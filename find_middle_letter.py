'''
Instructions:
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
'''


def get_middle(s):                 # Given function to complete
    n = int(len(s))                # 1. Find length of word
   
    if (n % 2 == 0):               # 2. for even no of chars, return index n/2 but -1 (index starts at 0) to n/2 but +1 
                                   #                          (as it will range to i previous than n/2 +1 which is n/1)
        return s[int(n/2)-1:int(n/2)+1] 
    else: 
        return s[int(n//2)]        # 3. for odd print the n/2 simply it is the middle index no            
