
name = "Prachi"
age = 21
marks = 88.5
is_student = True


my_list = [1, 2, 3]
my_tuple = (4, 5)
my_set = {1, 2, 3}
my_dict = {"name": "Prachi", "age": 21}


def greet(name):
    return f"Hello {name}"

print(greet(name))


squares = [x**2 for x in range(5)]
print(squares)


try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return f"{self.name} scored {self.marks}"

s1 = Student("Prachi", 90)
print(s1.display())