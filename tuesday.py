# functions
"""
-> functions are reusable blocks of code
-> we use the def keyword to declare variables
-> a function can accept zero or more parameters
-> it can output a value using the return keyword
"""

def sum(a, b):

    # allows a function to give an output
    # it also terminates the function
     return a + b

name = "Jane Doe"
total = sum(30, 30)

# print(total)


""" Decorators
-> design pattern that allows us to modify the functionality
of a function without modifying it
-> Can use the special @ symbol on functions
"""

def logger(func):
    def inner(a, b):
         a = a + 5
        #  add extra logic before executing decorated function
         print(f"Two digits ({a}, {b}) are being calculated")

        #  call/invoke the decorated function
         func(a, b)
    # we need to return the inner function for execution
    return inner

@logger
def calculate(a, b):
     print(a + b)
     return 10 + 10


# calculate(10, 10)


# Decorator B
def prettify(func):
    #  define inner function
    def inner():
        #  some additional logic
        print("Function is decorated")
        #  execute the original function
        func()
    return inner

@prettify
def simple_func():
     print("I am a simple function")
def ask_question():
     print("Ian is asking a question")

ask_question()

simple_func()


# decorate the simple function
# decorated_func = prettify(simple_func)

# # call the decorated function
# decorated_func()


# app = Flask(__name__)

# @app.get('/users')
# @jwt_required
# def get_users():
#     #  logic to get users from db
#     return []
