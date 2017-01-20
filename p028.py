#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13
#It can be verified that the sum of the numbers on the diagonals is 101.
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def p028():
    
    #notice that the upper right corner of a n x n grid is n^2
    #going backwards, upper left corner is n^2 - (n-1)
    #similarly, lower left corner is n^2 - 2(n-1)
    #and finally lower right corner is n^2 - 3(n-1)
    #thus, one ring contributes 4n^2 - 6(n-1)
    
    SIZE = 1001
    ans = 1
    ans += sum(4*i*i - 6*(i-1) for i in range(3,SIZE+1,2))
    
    return ans

if __name__ == "__main__":
    
    res = p028()
    print "diagonal sum: ", res