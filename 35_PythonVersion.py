f = open("35_New File.txt", "x")

f.write("\nThis will be appended to what was in the file\n")

f = open("35_FileHandling.txt", "r")
print(f.read())