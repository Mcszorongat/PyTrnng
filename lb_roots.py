def sqrt1(x):
    guess = x
    i = 0
    while guess * guess != x and i<20:
        guess = (guess + x/guess)/2.0
        i += 1
    return guess


def sqrt2(x):
    if x<0:
        raise ValueError(
            "Cannot compute square root of" f"negative number {x}")
    guess = x
    i = 0
    while guess * guess != x and i<20:
        guess = (guess + x/guess)/2.0
        i += 1
    return guess

import sys

def main():
    print(sqrt1(9))
    print(sqrt1(2))
    try:
        print(sqrt1(-1))
    except ZeroDivisionError:
        print("Cannot compute the square root of a negative number")
    print("Program execution continues normally here")
    
    try:
        print(sqrt2(-1))
    except ValueError as e:
        print(e, files=sys.stderr)

if __name__ == "__main__":
    main()
