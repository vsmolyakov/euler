#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

def p019():
    
    res = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                res += 1
    
    return res
    
if __name__ == "__main__":
    
    res = p019()
    print "num sundays: ", res
                

