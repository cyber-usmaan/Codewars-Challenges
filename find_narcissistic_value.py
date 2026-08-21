def narcissistic( value ):
    
    l = len(str(value))
    n = value
    sum=0
    m = 0
    
    while n > 0:
        m = n % 10
        sum = sum + (m ** l)
        n = n//10
    
    if sum == value:
        return True
    else:
        return False
