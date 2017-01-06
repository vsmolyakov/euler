#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import eulerlib

def p007():
    
    i = 2
    primes = []
    while len(primes) < 10001:
        if eulerlib.is_prime(i):
            primes.append(i)
        i=i+1
                    
    return primes
        
    
if __name__ == "__main__":
    
    primes = p007()
    print "10,001st prime: ", primes[-1]