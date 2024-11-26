# this is a single line comment in py

""" -> this is docstring
we can use this to add multiline comment
"""

print("Intro to python")

# Datatypes

# 1. str
print("Jane")
print('Doe')

# string interpolation using f string
first_name = "Jane"
last_name = " Doe"
print(first_name + last_name)
print(f"{first_name} Doe".upper())
print(type(first_name))
# 2. bool -> True/False
print(3 > 4)
# i. Number operators (>,<,>=)
# ii. Logical operators (and, or, not)
# iii. Comparision operators (==, !=)
print(bool(None))
# 3. int -> whole numbers PEMDAS
print(type(3))

# 4. float -> decimal numbers
print(type(0.2))

# 5. list -> ordered collection of data are same as arrays in js
# could map, append, can be indexed
students = ['Sharon', 'John']

cars = []

students.append("Brian")

students[0] = 'Dennis'

print(students)

# 6. tuple -> lists that are immutable
colors = ('red', 'green', 'blue')

print(type(colors))

# 7. set -> immutable list of elements inside curly braces {}
# sets also only accept unique values
unique_students = {'Brian', 'Ian', 'Benjamin', 'Ian'}
empty_set = set()

print(type(empty_set))

print(unique_students)

# 8. dict
person = {
    "first_name": "Jane",
    "courses": ["Software", "DevOps"]
}

print(person['first_name'])
print(person.get('courses'))
# 9. None -> null and undefined


# functions
def greeting(name, age):

    print(f"Good evening {name} {age}")

# call/invoke
# keyword arguments
greeting(age=23,name="Rome")
