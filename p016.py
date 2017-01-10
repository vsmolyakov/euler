#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

def p016():

    max_num = str(2**1000)
    
    sum = 0
    for c in max_num:
        sum += int(c)
    
    return sum
    
    
if __name__ == "__main__":
    
    sum = p016()
    print "The sum is: ", sum