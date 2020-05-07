# str
# no char just string; sequence of unicode code points
# strs are immutable
import copy

printFlag = False
rows = 80
columns = 9
for i in range(rows):
    for j in range(columns):
        num = columns*i + j
        if num > 34 and num < 126 and printFlag or num > 160 and printFlag:
            if j < columns-1:
                print(num, "\t-\t", chr(num), "\t", end=" ")
            else:
                print(num, "\t-\t", chr(num))

a = "string a"
b = 'string b'
c = "the 'c' string"
d = r"What\you\see\        what\''you\get"
e = str(3.14)
f = "\u00E1"    # unicode hex
g = "\xE1"      # hex
h = "\341"      # octal
i = a + " " + b

print(a, b, c, d, e, a[3], type(a[3]), f, g, h, "| i =", i)


# byte
# sequence of bytes (ascii characters only)
print("\n-----------------------------------------BYTE------------------------------------------------------\n")
a = b"asd"
print(a[0], chr(97))
b = "próbaszó"
c = b.encode('UTF8')
d = c.decode('UTF8')
print(b, "|", c, "|", d, "|", b==d)


# tuple
# immutable so it can be a key in dict
print("\n-----------------------------------------TUPLE------------------------------------------------------\n")
a = (1, 2)
b = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]   # tuples in a list --> improved readability
c = (5,)                                # single-element tuple
d = ()                                  # empty tuple
e = 1, 2                                # parenthesis can be omitted eg.: returning multiple items "return a, b"
f, g = e                                # tuple unpacking, destructuring operation
h = "first"
i = "second"
h, i = i, h
print("a =", a, "| b[1][1] =", b[1][1], "| type(c) =", type(c), "| len(d) =", len(d), "| type(e) =", type(e),
    "| e = ", e, "| f g =", f, g, "| h i =", h, i,
    "| 2 in e =", 2 in e, "| 3 not in e =", 3 not in e)


# list
# sequence of objects, mutable, lots of methods
print("\n-----------------------------------------LIST------------------------------------------------------\n")
a = []                  # empty list
b = [None]
c = [1, "kettő", 3.0]
d = c                   # shallow copy / reference copy
e = copy.deepcopy(c)    # deep copy
f = c.append("négy")    # no return value

print(a, "|", b, "|", c, "|", d, "|", e[2], "|", f)

# dict
print("\n-----------------------------------------DICT------------------------------------------------------\n")
d0 = {}                             # empty dict
d1 = {'a' : 1, 'b' : 2, 'c' : 3}
d1['d'] = 4
print(d1, "| 'a' =", d1['a'], "| 'b' =", d1['c'])   # from python 3.7 insertion order

for letter in d1:
    print(letter, "-", d1[letter])  # iterates through the keys --> value


# range: sequence representing an arithmetic progression of integers
# range(start, stop, step) stop: exclusive, start: inclusive
# range(stop) / range(start, stop) / range(start, stop, step)
print("\n------------------------------------------RANGE----------------------------------------------------\n")
