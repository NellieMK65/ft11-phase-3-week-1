# Data Structures

""" Dictionaries -> dict
-> Similar to objects in JS
-> Collection of key-value pairs
-> We use curly braces to define dicts
"""

empty_dict = {}

person = {
    "name": 'John',
    "courses": ["Software", "DevOps"]
}

# accessing values
# square bracket
# print(person['name'])

# get method
# print(person.get('age'))

# adding new properties
person['age'] = 20

# update
person['name'] = 'Jane'

# remove/del
del person['courses']

# print(person)

# looping dicts
for key, value in person.items():
    print(f"KEY {key} -> VALUE {value}")

for key in person.keys():
    print(person[key])

""" Sets
-> unordered list of immutable elements inside curly braces
-> Every element is unique
"""

empyt_set = set()

cars = {'Audi', 'Bmw', 'Audi', 'Audi'}

colors = ['red', 'green', 'blue', 'red']

print(set(colors))

# loop through a set
for car in cars:
    print(car)

