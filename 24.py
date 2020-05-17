import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345', db='meitar', autocommit=True)
cursor1 = connection.cursor()

cursor1.execute("select * from students")


# cursor1.execute("delete from students where id = '456456456'")

# for row in cursor1:
#   print(row[1])


# cursor1.execute("insert into meitar.students values (456456456, 'David', 'Ben Haim', 43)")
def new_animal(cursor_to_execute):
    id_of_animal = input("enter animal id: ")
    name_of_animal = input("enter animal name: ")
    age_of_animal = int(input("enter animal age: "))
    cursor_to_execute.execute(f"insert into animals values ({id_of_animal},'{name_of_animal}',{age_of_animal})")


# get new cursor
cursor1 = connection.cursor()


def new_animal(cursor_to_execute):
    name_of_animal = input("enter animal name: ")
    type_of_animal = input("enter animal type: ")
    age_of_animal = int(input("enter animal age: "))
    cursor_to_execute.execute(f"insert into animals values ('{name_of_animal}','{type_of_animal}',{age_of_animal})")


def delete_animal(cursor_to_execute, animal_name):
    cursor_to_execute.execute(f"delete from animals where name = '{animal_name}'")


# new_animal(cursor1)

def show_animals(cursor_to_execute):
    cursor_to_execute.execute("select * from animals")
    for row in cursor_to_execute:
        print(f"name is {row[0]}, age is: {row[2]}, from type: {row[1]}")


# delete_animal(cursor1, "rexi")
new_animal(cursor1)
new_animal(cursor1)
show_animals(cursor1)
