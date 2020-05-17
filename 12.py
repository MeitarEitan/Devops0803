
a = int(input("enter first number: "))
b = int(input("enter second number: "))

try:
    print(a/b)
except ZeroDivisionError as e:
    print("couldn't divide by zero")


try:
    open("asdasdas")
except FileNotFoundError as e:
    print(e.args)
