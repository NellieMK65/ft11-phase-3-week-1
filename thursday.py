# O.O.P (Object Oriented Programming)

# Four principles of OOP (D.R.Y)
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

"""
-> Involves the use of classes and objects
-> It makes it easier to reuse code
-> It has methods and properties (attributes)
"""

# class - blueprint for how objects are created and how they behave
# syntax
class Person:
    # class attribute
    species = "Homo sapiens"


    # should always be present when creating classes in python
    # it always takes self as its first parameter
    # This method is always automatically called when a new instance
    # is created
    def __init__(self, name, age = 18):
        # instance attributes
        self.name = name
        self.age = age

    # instance method (use to define object behaviors)
    # it always takes self as its first parameter
    def walk(self, pace):
        print(f"{self.name} is walking at {pace}")

# create an instance of the class to get the object
person1 = Person("John", 27)

# person1.name = "John"

print(person1.name)
# accesing class attribute through the instance
print(person1.species)
# accessing class attribute through the class itself
print(Person.species)

person2 = Person("Dennis")

# person2.name = "Dennis"

print(person2.name)

person3 = Person(name="Jane")
person3.walk("13 miles per hour")
# updating the name
person3.name = "Amon"

print(person3.name)



person4 = {
    "name": "Jane"
}


# print(person4['name'])

person4['name'] = 'Blessing'

# print(person4)

class Meeting:

    def __init__(self, time, cohort, name, host):
        self.time = time
        self.cohort = cohort
        self.name = name
        self.host = host

    def record(self):
        print(f"Recording started, it will be saved in {self.host} drive")

    def raise_hand(self):
        # logic raise hand
        pass

four_by_one = Meeting("10 A.M - 11 A.M", "SDFT11", "4:1", "Nelson")

four_by_one.record()
