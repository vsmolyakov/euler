#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def prime_factors(n):
    
    i=2
    factors = []    
    while i*i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.append(i)    
    if (n > 1):
        factors.append(n)
        
    return factors

def p003():

    max_num = 600851475143      
    factors = prime_factors(max_num)
    return factors
    
if __name__ == "__main__":
    
    factors = p003()
    print "max factor: ", max(factors)