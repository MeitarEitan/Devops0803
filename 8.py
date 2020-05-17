myFile = open("newFile.txt", "r")
allLines = myFile.readlines()

for line in allLines:
    print(line, end='')
myOtherFile=open("newFile.txt","a")
myOtherFile.write("\nthis is the last line")
myOtherFile.close()
myFile.close()

inputUser = input("Enter your name:")
myNewFile=open("names.txt","w")
myNewFile.write(inputUser)
myNewFile.close()

