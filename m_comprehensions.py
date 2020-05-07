# list
l1 = "ab cd ef gh ij kl mn op qr st uv wx yz".split()
C = [sum(bytes(word, "utf8")) for word in l1]
print(C, type(C))

# set
S = {sum(bytes(word, "utf8")) for word in l1}
print(S, type(S))

# dict
letterToNumber = {
     "a" : "first",
    "b" : "second",
    "c" : "third",
    "d" : "fourth"}
numberToLetter = {val : key for key, val in letterToNumber.items()}

print(letterToNumber)
print(numberToLetter)
