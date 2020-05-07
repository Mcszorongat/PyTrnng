from itertools import count, islice
from math import sqrt

def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x%i == 0:
            return False
    return True

def primes(x):
    return islice((p for p in count() if is_prime(p)), x)

print(list(primes(1000))[-10:])

print(sum(primes(1000)))

print(any([True, True]))
print(any([True, False]))
print(any([False, False]))  # is there a TRUE
print(all([True, True]))    # are all of them TRUE
print(all([True, False]))
print(all([False, False]))

print("Is there a prime between 1328 and 1361:", any(is_prime(x) for x in range(1328, 1361)))

monday = [11, 12, 13, 14, 15, 16, 17, 17, 17, 16, 16, 15, 14, 13, 12, 11, 11]
tuesday = [x*2-10 for x in monday]
print(monday, tuesday)
for item in zip(monday, tuesday):
    print(item, type(item))

for d1, d2 in zip(monday, tuesday):
    print(f"Hourly average is {(d1 + d2)/2}°C")

wednesday = [x*2-20 for x in tuesday]

for temps in zip(monday, tuesday, wednesday):
    print(f"min={min(temps):4.1f}\t max={max(temps):4.1f}\t avg={sum(temps)/len(temps):4.1f}")

from itertools import chain
temperatures = chain(monday, tuesday, wednesday)
print(monday, tuesday, wednesday)   # concatenation
print(list(temperatures))           # lazy concatenation

from md_lucas import lucas
from time import perf_counter as tc
start = tc()
for x in (p for p in lucas() if is_prime(p)):
    print(x, "time:", tc()-start)