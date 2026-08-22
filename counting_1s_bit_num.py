'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

def count_bits(n):

    bil = []
    while n > 0:
        if n % 2 != 0:  #check if for 1s in binary and add to list as string
            bil.append("1")
        n = n // 2      #keep dividing the string by 2
        
    return len("".join(bil)) #returning the length of string which is equal to no of 1s in binary of that num

'''
alternate solution
def count_bits(n):
    return bin(n).count("1")
'''
