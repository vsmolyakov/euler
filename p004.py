# -*- coding: utf-8 -*-
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def p004():
    
    ans = 0    
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > ans:
                ans = k
    
    return ans


if __name__ == "__main__":
    
    ans = p004()
    print "largest palindrome: ", ans
                
            