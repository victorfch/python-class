sizeCharactersToShow = 2
f = open("read.txt", "r")
print(" ---- Ways to read a file ----")
for line in f:
    print(line)
f.close()

keepReading = True
file2 = open("read.txt", "r")
while keepReading:
    line = file2.readline()
    print(line)
    if not line:
        keepReading = False
file2.close()
