input_from_user = input("enter your name: ")
print("Your name is: " + input_from_user)
age = input("What is your age")


def my_own_printer(to_print):
    print("-----")
    print(to_print)
    print("------")


my_own_printer(input_from_user)


def square(x):
    return x * x
