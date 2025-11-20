filename="filewrite.txt"
print(f"This will erase the contects of {filename}")
print("Opening the file")
target= open(filename,'w')
print("Truncating the file")
target.truncate()
n = int(input("Enter the number of lines: "))
for i in range(0, n):
    line = input(f"Line {i + 1} :")
    target.write(line)
    target.write("\n")

print("Finally close the file")
target.close()

from_file="textFile1.txt"
