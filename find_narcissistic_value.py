'''
Instructions:
A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
We will restrict ourselves to decimal (base 10).

For example, take 153 (3 digits), which is narcissistic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

The Challenge:

Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10.
This may be True and False in your language, e.g. PHP.
Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

'''

#my solution
def narcissistic(value):
    
    l = len(str(value)) # 1. Storing length of number
    n = value
    sum=0
    m = 0
    
    while n > 0:  # 2. Looping for each value to be seperated by mod and raised to the power of lenght of the num
        m = n % 10 
        sum = sum + (m ** l)
        n = n//10
    
    return sum == value: # 3. Comparing the sum of each digit raised to the power of that number to with sum
    # True for Narcissistic Number and False for Non-narcissistic Number
