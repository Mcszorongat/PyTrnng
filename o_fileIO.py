import sys
print(f"Default encoding: {sys.getdefaultencoding()}")     # default encoding of different systems can be also differ

f1 = open("o_textfile.txt", mode= 'wt', encoding='utf8')     # w - write r - read a - append t - text b - binary
print(f1.write("1st line, "))  # returns the character written into the file
f1.write("second part.\n")
f1.write("2nd line of file.")
f1.close()                      # it'll be available for other programs

# read the file back
f2 = open("o_textfile.txt", mode='rt', encoding='utf8')
print("First read:\n", f2.read(5))
print("Second read:\n", f2.read(25))
print("Third read:\n", f2.read())
print("Fourth read:\n", f2.read())
print("end")
# back to the beginning:
f2.seek(0)                      # return value new pointer position
print("\nOnce again:\nFirst read:\n", f2.read(5))
print("Second read:\n", f2.read(25))
print("Third read:\n", f2.read())
print("Fourth read:\n", f2.read())
print("end\n\nreadline method:\n")

f2.seek(0)                      # necessary for the readline as well
print("First line: ", f2.readline())
print("Second line: ", f2.readline())

print("\nReaading all the lines into a list:")
f2.seek(0)
l1 = f2.readlines()
print(l1)
f2.close()

# append
f3 = open("o_textfile.txt", mode='at', encoding='utf8')
f3.writelines([
            "\nAppended third line", "\n",
            "And a fourth as well.",
             ])