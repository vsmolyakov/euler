#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def p006():
    
    sum1, sum2 = 0, 0
    for i in range(1,101):
        sum1 += i
        sum2 += i**2
        
    result = sum1**2 - sum2
    
    return result
    
    
if __name__ == "__main__":
    
    res = p006()
    print "result: ", res