# don't relie on the order of the items eventhough from 3.7 it has to be the order of addition
d0 = {}                                     # empty dict
d1 = {'a' : 1, 'b' : 2, 'c' : 3}
d1['d'] = 4                                 # adding new element
for letter in d1:
    print(letter, "-", d1[letter])          # iterates through the keys --> value
#
l2 = [("Alpha", 1), ("Bravo", 4), ("Charlie", 4)]
print(l2)
d2 = dict(l2)
print(d2)
#
d3 = d2.copy()
d2["Bravo"] = 2
d4 = dict(d2)
d2["Charlie"] = 5
print(d3)
print(d4)
#
d5 = {"Charlie" : 3, "Delta" : 4, "Echo" : 5}
d2.update(d5)
print(d2)
for key in d2:              # d2.key()
    print(key)
for value in d2.values():
    print(value)
for key, value in d2.items():
    print(f"key: {key}\t and \t value:{value}")
#
print("Alpha" in d2)        # works on keys
print("Foxtrot" in d2)      # not element
print("2" in d2)            # not a key
del d3["Alpha"]
print(d3)