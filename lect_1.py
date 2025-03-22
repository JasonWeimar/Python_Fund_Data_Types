import math


# String can be created using single or double quotes.
# Naming Convention: snake_case
# Variable name rules: Cant start with a number. Cant have a hyphen. Cant use reserved keywords (ex. print, for)

# Literal Assignment:
string_1 = "Hello World"

# Constructor function (casting)
string_2 = str("Another greeting")

# Print Function: see value of any variable
print(string_1)

# Type Function: Will print out whatever the data type is that you pass to it
print(type(string_1))

# Concatenation: Adding two strings together
hello = "hello"
world = "world"
hello_world = hello + " " + world
print(hello_world)

# Concatenation: Using F-String
print(f"{hello} big {world}")

# Type Error: Python cant differentiate strings from numbers and will need to have a num converted to string
num = 10
sentence = "my age is "
print(sentence + str(num))

# --- String Methods: ---

# split:
stack = "Python World"
print([*stack])
# upper/lower/title:
print(stack.upper())
print(stack.lower())
print(stack.title())

# center: Handy for debugging to help find what you're looking for
print(stack.center(50, "*"))

# length:
print(len(stack))

# strip: removes leading and trailing white space
whitespace_string = "     hello     "
print(whitespace_string)
print(whitespace_string.strip())

# String Indicies / Index Ranges:

guitar = "fender"
print(guitar[0])
# slicing with index ranges
print(
    guitar[1:3]
)  # known as a 'slice' of a string (leaving out the second number assumes you want to go to end of string)
print(guitar[-1])  # Returns last element

# ----- Office Hour 2 finishes Lecture 1 -----

# Integers and Floats:

# Integer literal assignment:
num = 4

# Constructor Function (casting):
string_num = "4"
int_num = int(string_num)
print(type(int_num))

# Float Literal Assignment:
pi = 3.15159
print(type(pi))

# Constructor Function (casting):
float_num = float(num)
print(float_num)

# Arithmetic Operations -  +, -, *, /, **, //

print(2**3)
# output = 8

print(5 // 2)
# output = 2 (floor - chops off decimal and converts value to integer)

# Assignment Operators -  +=, -+, *=, /=

other_num = 4
new_num = 2
new_num += other_num
print(new_num)
# output = 6
# These are shorthand for ex. new_num = new_num + other_num

# Built-in Functions for Numbers:


# abs, round

print(abs(-3.5))
# output = 3.5 (Absolute Value: The distance from 0 (ex. The distance from -3.5 to 0 = 3.5))
print(round(3.14159))
# output = 3 (.5 or above rounds up, .49 or below rounds down)


#  Math Module: (must import at top of file) - sqrt, ceil, floor

# sqrt: provides the Sqare Root
print(math.sqrt(9))
# output = 3

# cei: Go to next highest int (up)
print(math.ceil(2.000001))
# output = 3

# floor: Go to next lowest int (down)
print(math.floor(35.99999))
# output = 35


#  Booleans: Python Capitalizes Bools

is_awake = False

# Constructor Function (casting):

is_sleeping = bool(True)
print(is_sleeping)
# output = True


# None type: None Data Type is the absence of a value (JavaScript equivelant to Null)

# None Literal Assignment:

email = None
print(type(email))
# output = NoneType

# Why use None?: As a placeholder (to start with an absence, but is to be filled in later)
