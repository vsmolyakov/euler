#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import fractions

def p005():    
    # lcm(x,y) = x * y / gcd(x,y)
    ans = 1
    for i in range(1,21):
        ans = ans * i / fractions.gcd(ans, i)

    return ans                

if __name__ == "__main__":
    
    lcm = p005()
    print "lcm: ", lcm