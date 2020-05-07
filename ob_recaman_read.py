import sys


def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf8')
#        series=[]
#        for line in f:
#            a = int(line.strip())       # strips the line end character
#            series.append(a)
        return [int(line.strip()) for line in f]
    finally:
        f.close()
#    return series


def read_series2(filename):
    with open(filename, mode='rt', encoding='utf8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series2(filename)
    print(series)


if __name__ == "__main__":
    main("ob_recaman.txt")