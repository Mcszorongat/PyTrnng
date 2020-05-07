DIGIT_MAP = {
    "zero" : '0',
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9',
}

def convert1(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x

def convert2(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except KeyError:
        x = -1
    except TypeError:
        x = -2
    return x

def convert3(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError):
        pass
    return x

def convert4(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError):
        return -1

import sys

def convert5(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as exc:
        print(f"Conversion error: {exc!r}", file=sys.stderr)    # !r - wrapper representation
        return -1

def convert6(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as exc:
        print(f"Conversion error: {exc!r}", file=sys.stderr)    # !r - wrapper representation
        raise

import math

def string_log(s):
    v = convert6(s)
    return math.log(v)