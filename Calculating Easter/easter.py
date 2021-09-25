# Names (me, Partner 1, Partner 2): Shima Abdulla, Luis Alfaro, Henry Chau
"""This function calculates the  Gregorian Easter using Gauss's algorithm.
 y: y represents a four digit integer of the year by which we are attempting to determine Easter for (only arguement)
 ideally this would return the date by which easter falls on the determined year. It raises error when year is smaller than 1583 as the greogorian calendar was only adopted after that
"""

import sys


def easter_date(y):
    if y < 1583:
        raise ValueError("Year must be after 1583")
    a = y % 19
    b = y % 4
    c = y % 7
    k = y // 100
    p = (13 + 8*k)// 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19*a  + M) % 30
    e = (2*b + 4*c + 6*d + N) %7
    # r is March
    r = 22 + d + e
    # s is April
    s = d + e - 9
    
    if d == 29 and e == 6 and s == 26:
        r = 19
    elif (d == 28 and e == 6 and s == 25 and (11*M + 11) % 30 < 19): 
        s = 18
    date = f"March {r}" if r < 32 else f"April {s}"
    return date

if __name__ == "__main__":
    try:
        year = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a year as a command-line argument")
    except ValueError:
        sys.exit("could not convert", sys.argv[1], "into an integer")
    print(easter_date(year))
