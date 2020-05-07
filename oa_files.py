import sys

f = open(sys.argv[1], mode='rt', encoding='utf8')
for line in f:
    sys.stdout.write(line) # print(line)
f.close()