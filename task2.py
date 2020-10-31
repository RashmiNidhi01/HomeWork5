import sys

file = open("book.txt", "r", errors ='ignore') # open file
charcount = {} #dictionary to hold char counts
validchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # only these counted

for i in range(65,91): # lowercase range
    c = (chr(i)) # the chars a-z
    charcount[c] = 0

for line in file:
    words = line.split(" ")
    for word in words:
      chars = list(word)
      for c in chars:
          if c.isalpha():
              if c.islower():
                  c = c.upper()
              if c in validchars:
                  charcount[c] += 1

old_stdout = sys.stdout
log_file = open("summary.txt", "w")
sys.stdout = log_file
flag = 0
for key, value in sorted(charcount.items()):
    if value == 0:
        flag = 1
    print(key, value)
if flag == 1:
    print("\nIt doesn't have all letters.")
else:
    print("\nIt has all letters")
sys.stdout = old_stdout
log_file.close()
file.close() # close file
