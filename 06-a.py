import os.path
import sys

fname = input("Enter the filename: ")

if not os.path.isfile(fname):
    print("File ", fname, " doesn't exists.")
    sys.exit(0)

infile = open(fname,"r")
linelist = infile.readlines()
for i in range(len(linelist)):
    print(i+1, " : ", linelist[i])

word = input("Enter a word: ")
cnt = 0
for line in linelist:
    cnt += line.count(word)

print("The word ", word, " appears ", cnt, " times in the file.")