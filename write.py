filename="filewrite.txt"
print(f"This will erase the contects of {filename}")
input("?")

print("Opening the file")
target= open(filename,'w')
print("Truncating the file")
target.truncate()
print("Enter 3 lines")
line1=input("Line 1 :")
line2=input("Line 2 :")
line3=input("Line 3 :")


target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print("Finally close the file")
target.close()

from_file="textFile1.txt"
