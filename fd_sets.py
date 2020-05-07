# an unordered, mutable collection of immutable elements
s1 = {1, 3, 5, 7, 'asd'}
print(s1)                   # unordered
s2 = set()                  # s2 = {} --> dict
s3 = set([1, 1, 2, 3, 4, 4, 5])
print(s3)
l3 = list(s3)
print(l3)                   # duplicates are removed
print(1 in s3)
s3.add(6)
print(s3)
s3.update([7, 7, 8 ,9])
print(s3)
s3.remove(9)                # element has to be present
print(s3)
s3.discard(9)               # does not produce error if element is missiing
#
s11 = {2, 4, 6, 8}          # even under 10
s12 = {1, 3, 5, 7, 9}       # odd under 10
s13 = {2, 3, 5, 7}          # primes under 10
print(s11.union(s12))       # A + B
print(s11.intersection(s13))# A * B
print(s11.difference(s13))  # A - B
print(s11.symmetric_difference(s13) == s11.union(s13).difference(s11.intersection(s13)))    # A + B - A * B
print(s13.issubset(s11))    # false because of 2
print(s11.isdisjoint(s12))  # odd or even