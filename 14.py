def get_age():
    user_age = int(input("Enter your age: "))
    if user_age < 0:
        raise ValueError("Age cannot be negative")

    try:
        get_age()
    except ValueError as e:
        print("failed to get age because of: " + str(e.args))


get_age()
