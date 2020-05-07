import sys

iterable = ['a', 'b', 'c', 'd', 'e']
iterator = iter(iterable)

for _ in iterable:
    print(next(iterator))

try:
    next(iterator)
except StopIteration as e:
    print(e, file=sys.stderr)