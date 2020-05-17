def saveNames():
    inputUser = input("Enter your name:")
    myNewFile = open("names.txt", "a")
    myNewFile.write(inputUser + "\n")
    myNewFile.close()


def printNames():
    file = open("names.txt", "r")
    for name in file.readlines():
        print(name, end=" ")
    file.close()


saveNames()
saveNames()
saveNames()
printNames()
