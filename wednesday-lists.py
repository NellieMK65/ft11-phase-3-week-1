""" Lists -> []
-> ordered collection of items
-> every item has a position known as the index
-> every list starts from index 0
"""

nums = [1, 2, 3]

# add element to end of list
nums.append(23)

print(nums)

# adding element at any any postion
nums.insert(2, 21)

print(nums)

# removing last element using pop
last = nums.pop()

print(last)
print(nums)

# remove element by value
nums.remove(21)

print(nums)

colors = ['red', 'green', 'blue', 'red']

# slice

deleted = colors[0:2]

print(deleted)

# print(colors)

# iterating

# modified = map(fn, list) -> syntax

# using normal functions
def capitize(word):
    return word.upper()

capitalized = map(capitize, colors)

print(list(capitalized))


# using lambda
modified = map(lambda word: word.upper(), colors)

print(list(modified))

# ! Assignment -> implement reduce and filter methods


""" Tuple -> ()
-> immutable list
"""

# 3 + (4 * 3) / 3

# When you have single element in a tuple, you must add a comma at the end
students = ('Amon', 'Brian')

print(type(students))
