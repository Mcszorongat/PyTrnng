# while
x = 10
statement = True
while statement:
    print(x)
    x -= 1
    statement = x>0

print("\n________________________________________________\n")

x = 10
while x:
    print(x)
    x-=1

print("\n________________________________________________\n")

while True:
    x += 1
    print(x)
    if x == 10:
        break
print("\n________________________________________________\n")

# for
for i in range(10):
    print(i + 1)

print("\n________________________________________________\n")

for j in range(10, 0, -1):
    print(j)
    if j == 5:
        break