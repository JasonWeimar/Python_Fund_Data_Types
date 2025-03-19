# String Literals

print("This is a sample String")

# Concatenating Strings
name = "Jason"
print("My name is", name)

name = "Rusty"
print("My name is " + name)

# Type Casting

user_name = 303
print("My Username is ", user_name)

# Python doesn't know how to add a String to a Number (but it can add two strings together)

# print("My Username is " + user_name)

# print("Hello " + 42)  # Output: TypeError
print("Hello " + str(42))  # Output: Hello 42

#  String Interpolation (injecting Variables into a string)

# Option 1: F-String (Literal String Interpolation)

first_name = "Jason"
last_name = "Weimar"
age = 37
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# Option 2: String.Format (calls the .format method on a string then passes in arguments in the order they should fill the {} placeholders.)

first_name = "Rusty"
last_name = "Brown"
age = 7
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
print("My name is {} {} and I am {} years old.".format(age, last_name, first_name))

# %-Formatting: Old method of string interpolation that uses the '%' as a placeholder (%s for a string and %d for a number). After the String, a single '%' separates the string to be interpolated from the values to be inserted.

hw = "Hello %s" % "world"  # with literal values
py = "I love Python %d" % 3
print(hw, py)  # Output: Hello world I love Python 3

name = "JSON303"
age = 37
print("My name is %s and I'm %d" % (name, age))

# Built in String Methods:

x = "hello world"
print(x.title())  # Output: "Hello World"

y = ("Jason", "Weimar")

z = "|"

# List of commonly used String Methods:

print(x.upper())  # Returns a copy of the string with all the characters in uppercase
print(x.lower())  # Returns a copy of the string with all the characters in lowercase
print(x.count("o"))  # Returns number of occurrences of a substring in string

print(
    x.split()
)  # Returns a list of values where string is split at the given character. Without a parameter the default split is at every space.

print(
    x.find("e")
)  # Returns the index of the start of the first occurrence of substring within string

print(
    x.isalnum()
)  # Returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters/numbers only). Strings that include spaces and punctuation will return False for this method. Similar methods include: .isalpha(), .isdigit(), .islower(), .isupper()

print(
    z.join(y)
)  # Returns a string that is all strings within our set (in this case a list) concatinated

print(
    x.endswith("d")
)  # Returns a boolean based upon wheter the last characters of string match substring
