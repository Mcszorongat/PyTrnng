million_squares = (x*x for x in range(1, 100001))   # () instead of [] list constructors so it will run lazy

for i in range(10):
    for j in range(5500):
        next(million_squares)
    print(next(million_squares))

print(sum(x*x for x in range(1, 1000001)))