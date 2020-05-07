# píthon iterators
def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    print("I'm about to yield 2")
    yield 2
    print("I'm about to yield 5")
    yield 5
    print("I'm about to yield 7")
    yield 7
    print("About to return")

def main():
    g1 = gen1()
    g2 = gen2()
    print(g1)
    for _ in range(3):
        print(next(g1))
    for i in range(3):
        print(f"call: {i}")
        print(next(g2))

if __name__ == "__main__":
    main()
