"""
Q206: If a list passed into a function
as an argument, deleting any of its elements
inside the function using the del instruction:


Answer:  will affect the argument



---------------
E.g:

"""


def my_function(food):
    for x in food:
        print(x)
    del food[0]  # delete the first item


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print(fruits)  # ["banana", "cherry"]
