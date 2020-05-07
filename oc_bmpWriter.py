def _int2byte(i):
    """Converts a 32-bit integer to four bytes in little endian format"""
    # & bitwise-and
    # >> right shift
    return bytes((i & 0xff, i >> 8 & 0xff, i >> 16 & 0xff, i >> 24 & 0xff))


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.
    
    Args:
        filename:
            the name of the bmp file to be created

        pixels:
            rectangular image stored as sequence of rows
            each row must be an iterable series in the range 0-255

    Raises:
        ValueError:
            If any of the integer values are out of range

        OSError:
            If the file couldn't be written
    """

    height = len(pixels)
    width = len(pixels[0])




    with open(filename, mode='wb') as bmp:
        bmp.write(b'BM')

        sizeBookmark = bmp.tell()           # stores the current position in the file so later can be used
        bmp.write(b"\x00\x00\x00\x00")     # writing placeholders for the future size

        bmp.write(b"\x00\x00")             # two pairs of zero bytes
        bmp.write(b"\x00\x00")

        pixelOffsetBookmark = bmp.tell()    # beginning of the pixel data
        bmp.write(b"\x00\x00\x00\x00")     # we don't know that yet so --> placeholder

        # Image Header
        bmp.write(b"\x28\x00\x00\x00")      # image header size in bytes: 40 (little endian, LSB goes first)
        bmp.write(_int2byte(width))         # image width
        bmp.write(_int2byte(height))        # image height
        bmp.write(b"\x01\x00")              # number of image planes
        bmp.write(b"\x08\x00")              # bits per pixel (8 for gray scale)
        bmp.write(b"\x00\x00\x00\x00")      # no compression
        bmp.write(b"\x00\x00\x00\x00")      # zero for uncompressed images
        bmp.write(b"\x00\x00\x00\x00")      # unused pixels per meter
        bmp.write(b"\x00\x00\x00\x00")      # unused pixels per meter
        bmp.write(b"\x00\x00\x00\x00")      # use whole color table
        bmp.write(b"\x00\x00\x00\x00")      # all color are important

        # color palette - linear gray scale
        for c in range(0, 256):
            bmp.write(bytes((c, c, c, 0)))  # b g r 0

        # pixel data
        pixelDataBookmark = bmp.tell()
        for row in reversed(pixels):        # BMP files are bottom to top
            rowData = bytes(row)
            bmp.write(rowData)
            padding = b"\x00" * ((4 - (len(row) % 4)) % 4)  # Pad row to multiple of four bytes
            bmp.write(padding)

        # end of file
        eofBookmark = bmp.tell()

        # fill in file size placeholder
        bmp.seek(sizeBookmark)
        bmp.write(_int2byte(eofBookmark))

        # fill in pixel offset placeholder
        bmp.seek(pixelOffsetBookmark)
        bmp.write(_int2byte(pixelDataBookmark))

import math

def mandel(real, imag):
    x = 0
    y = 0
    for i in range(1, 257):
        if x*x + y*y > 4.0:
            break
        xt = real + x*x - y*y
        y = imag + 2.0*x*y
        x = xt
    return int(math.log(i)*256/math.log(256)) - 1


def mandelbrot(sizeX, sizeY):
    return [[mandel((3.5*x/sizeX) - 2.5, (2.0*y/sizeY) - 1.0) for x in range(sizeX)] for y in range(sizeY)]

def dimensions(filename):
    with open(filename, mode='rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError(f"{filename} is not a BMP-file!")
        f.seek(18)
        wBytes = f.read(4)
        hBytes = f.read(4)

        return (_byte2int(wBytes), _byte2int(hBytes))


def _byte2int(b):
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)


if __name__ == "__main__":
    pixels = mandelbrot(448, 256)
    write_grayscale("oc_BMP.bmp", pixels)
    print(dimensions("oc_BMP.bmp"))
