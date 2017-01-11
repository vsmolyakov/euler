#Find the sum of the digits in the number 100!

import math

def p020():
    
    n = math.factorial(100)
    res = sum(int(c) for c in str(n))
    
    return res
    
    
if __name__ == "__main__":
    
    res = p020()
    print "sum is ", res