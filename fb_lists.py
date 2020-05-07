a = []                      # empty list
b = [None]
c = [1, "kettő", 3.0]
print(a, "|", b, "|", c)

d = list(range(10))
print(d[-1])            # indexing the last element (1-based)
print(d[7:-1])         # slicing (end is exclusive)
print(d[7:])           # till the end
print(d[-1:0:-1])       # slice and reverse (-1 element)
print(d[-1::-1])        # all the elements