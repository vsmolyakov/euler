#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import eulerlib

def p010():
    
    max_num = 1999999
    
    res = sum(eulerlib.list_primes(max_num))
    
    return res
    
if __name__ == "__main__":
    
    sum = p010()
    print "sum of primes: ", sum