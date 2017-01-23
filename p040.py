# -*- coding: utf-8 -*-
#An irrational decimal fraction is created by concatenating the positive integers:
#0.123456789101112131415161718192021...
#It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def p040():
    
    s = "".join(str(i) for i in range(1,1000000))
    prod = 1
    for i in range(7):
        prod *= int(s[10**i - 1])

    return prod    

if __name__ == "__main__":
    
    res = p040()
    print "product: ", res