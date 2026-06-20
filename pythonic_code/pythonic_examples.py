"""
Some examples of code that is considered "Pythonic"   # This entry docstring is pythonic haha
"""

print("Example 1: Loops")
fruits = ["apple", "peach", "fig", "pawpaw"]

# Do this
for fruit in fruits:
    print(fruit)

# Not this
for i in range(len(fruits)):
    print(fruits[i])
# This second approach looks like code from compiled languages like Java or C but is not considered "Pythonic" because it is more verbose and less readable than the first approach.
# Besides there is no gain in performance


















print("Example 2: Checking if an element is in a list")
veggies = ["squash", "corn", "peas"]

# Do this
has_corn = "corn" in veggies
print(has_corn)

# Not this
has_corn = False
for veggie in veggies:
    if veggie == "corn":
        has_corn = True
print(has_corn)



















print("Example 3: Checking if all items in a list exist")
attendance_count = [25, 60, 0, 18, 54, 2]

# Do this
attendees = all(attendance_count) # That's important to know all(), it cleans up a codebase and makes it more readable.

# Not this
attendees = True  # set a flag
for count in attendance_count:
    if count == 0:
        attendees = False # reset the flag if we find a zero
print(attendees)

























print("Example 4: Comparisons")
calculation_complete = False

# Do this: more human readable 
if not calculation_complete:
    print('Calculation is not complete')

# Not this
if calculation_complete == False:
    print('Calculation is not complete')

























print("Example 5: List comprehensions")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Do this: just one line of code, more readable and optimized out of the box for performance
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Not this
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

























print("Example 6: Reading from a file")
file_name = "README.md"

# Do this: that's called a "context manager" 
with open(file_name) as readme: # close() is handled automatically when we exit the block of code
    print(readme.name)

# Not this
readme = open(file_name)
print(readme.name)
readme.close()

# THis will help to avoid memory leaks or any human error of forgetting to close an open buffer.This can lead to some security issues and performance problems in larger applications.






















print("Example 7: String formatting")
favorite_fruit = "nectarine"

# Do this
print(f'My favorite fruit is the {favorite_fruit}')

# Not this: older way of formatting strings, still works in Python3 but fstrings appears in Python 3.6
print('My favorite fruit is the {}'.format(favorite_fruit))

















# "Type hinting" - tells other developers and tools what types to expect

# Do this
def hello(name: str, age: int) -> str:
    return f"hello, {name}, you are {age} years old."

# Not this
def hello(name, age):
    return f"hello, {name}, you are {age} years old."

# Benefits of type-hinting:
# - Integration with IDEs
# - Documentation in the code itself
# - MyPy example (type_hints.py)