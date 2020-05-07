import math                     # for help module has to be imported

print("\n---------------------------START---------------------------\n")

x = math.sqrt(16**2)
print("x = ", x)

import math as m 
y = m.sqrt(x)
print("y = ", y)

from math import sqrt as sq
z = sq(y)
print("z = ", z)

print("10 / 5 = ", 10/5)        # floating point division operator
print("10 //5 = ", 10//5)       # integer division operator

print("2^100 = ", 2**100, "length = ", len(str(2**100)))

# integer
print("\n------------------------------INTEGER-------------------------------\n")
a = 20
b = 0b10100
c = 0x14
d = int(20.5)
e = int("10100", 2)             # base of the argument --> decimal
f = e
e += 5
print("a = ", a, ", b = ", b, ", c = ", c, ", d = ", d, ", e =", e, ", f =", f)

# float
print("\n------------------------------FLOAT-------------------------------\n")
a = 3.14
b = 6e23
c = 1.616e-35
d = float("nan")
e = float("-inf")
f = float("inf")
g = 2.0 + 2
print("a = ", a, ", b = ", b, ", c = ", c,
    ", d = ", d, ", e = ", e, ", f = ", f, ", g = ", g)

# none
a = None
print("a is", a, ": ", a is None)

# boolean
a = True
b = False
c = bool(2)
d = bool(-1.1)
e = bool(0)
f = bool([0, 0, 0])
g = bool([])
h = bool("False")
i = bool("")
print("a = ", a, ", b = ", b, ", c = ", c, ", d = ", d,
    ", e = ", e, ", f = ", f, ", g = ", g, ", h = ", h, ", i = ", i)

# relational operators
print("1==1:\t", 1==1, "\n1!=2:\t", 1!=2, "\n2>1:\t", 2>1, "\n1<2:\t", 1<2,
    "\n2>=2:\t", 2>=2, "\n2<=1:\t", 2<=1)