# -*- coding: utf-8 -*-
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

import eulerlib

def p015():
    
    #there are exactly N moves down and N moves to the right in a NxN grid
    #there 2N choose N ways of choosing the order assuming independent moves
    return eulerlib.binomial(40,20)
    
if __name__ == "__main__":
    
    res = p015()
    print "num of paths: ", res

