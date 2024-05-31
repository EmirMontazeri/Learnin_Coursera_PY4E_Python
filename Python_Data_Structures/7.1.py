# Write a program that reads a file and prints out the contents line by line in upper case.
fhand = open('BOOM.txt')
for Ln in fhand:
    Ln2 = Ln.rstrip()
    print(Ln2.upper())