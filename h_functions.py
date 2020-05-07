def square(x):
    return x*x

print(square(3))


# recursive function
print("---------------------------------------------")
def fact(x):
    if x>1:
        y = fact(x-1)
    else:
        y = 1
    return x*y

print(fact(3))


# arguments
print("---------------------------------------------")
def power(base, exponent=2):            # default value --> optional argument | arguments with default values follow the rest | executed only once, so exponent won't change
    return base ** exponent

print(power(2))
print(power(2, 3))                      # optional argument
print(power(2, exponent=4))             # positional argument, keyword argument
print(power(exponent = 5, base = 2))    # order of keyword arguments can be changed