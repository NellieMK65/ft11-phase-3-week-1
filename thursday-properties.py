
class Person:
    # class attribute
    # this is shared between all instances
    species = "Homo sapiens"


    # should always be present when creating classes in python
    # it always takes self as its first parameter
    # This method is always automatically called when a new instance
    # is created
    def __init__(self, name, age = 18):
        # instance attributes
        self._name = name
        self._age = age

    # instance method (use to define object behaviors)
    # it always takes self as its first parameter
    def walk(self, pace):
        print(f"{self._name} is walking at {pace}")

    def save(self):
        # write SQL logic to save info to db
        pass

    # properties
    # getter method for age
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name.upper()

    # setter method for age
    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("The age must be over 18")
        self._age = value

    # class method
    @classmethod
    def sleep(cls, name):
        # cls is the entire class instance
        # you can use the cls parameter to create an instance of the
        # class
        new_person = cls(name)
        print(f"{new_person.name} is sleeping")


# properties -> attributes controlled by methods
person1 = Person("Kevin", 17)

print(person1.name)

# update age property
person1.age = 23

print(person1.age)
