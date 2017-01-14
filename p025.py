#F12 = 144, The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def p025():
    
    a = 1
    b = 1
    i = 1
    
    while len(str(a)) != 1000:
        a, b = b, a+b
        i+= 1
        
    return i
    
if __name__ == "__main__":
    
    res = p025()
    print "ith fib: ", res