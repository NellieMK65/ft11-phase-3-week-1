"""Control flow
-> This allows us to alter the normal execution flow
-> Conditional operators (if)
-> Repetition (while, for)
"""

age = 9
name = "Jane"

if age < 10 or name == "John":
    print("Kshs 50")
elif age < 18:
    print("Kshs 100")
else:
    print("200 Kshs")



# for
# for i in range(5):
#     print(i)
cars = ['Bmw', 'Jaguar', 'Audi']

for car in cars:
    print(car)

i = 0
while i < 5:
    print(i)
    i += 1
