import sys
from itertools import count, islice

def sequence():
    """Generates Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c<0 or c in seen:
            c = a + n   
        a = c


def write_sequence(filename, num):
    """Writes Recamans's sequence to a text file."""
    print(filename, type(filename), num, type(num))
    f = open(filename, mode='wt', encoding='utf8')
    f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))
    f.close()

def write_sequence2(filename, num):
    """Writes Recamans's sequence to a text file."""
    with open(filename, mode='wt', encoding='utf8') as f:
        f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))

if __name__ == "__main__":
    write_sequence2("ob_recaman.txt", 120)
    #write_sequence(sys.argv[1], int(sys.argv[2]))