# BUILT-IN
print("print")


# GLOBAL
import math
print(math.pi)


# LOCAL
def fcn(num):
    multiplier = 2
    print(multiplier)
    return num * multiplier

# ENCLOSING
a = 5
fcn(5)
print(a)