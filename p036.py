#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)

def is_double_palyndromic(n):
    
    s = str(n)
    if s != s[::-1]:
        return False
    b = bin(n)[2:]
    return b == b[::-1]


def p036():
    
    res = sum(i for i in range(1000000) if is_double_palyndromic(i))
    return res
    
if __name__ == "__main__":
    
    res = p036()
    print "number of double palyndromes: ", res