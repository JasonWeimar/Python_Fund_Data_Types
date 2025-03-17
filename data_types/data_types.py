# primitive data types:

# Boolean Values - Assesses the truth value of something. It has only two values: True & False (note the uppercase T/F)

is_hungry = True
has_freckles = False

# Numbers - Integers (Whole Numbers), Floating Point Numbers (commonly known as decimal numbers), and Complex Numbers

age = 35  # storing an int
weight = 160.57  # storing a float

#  Strings - Leteral text

name = "Jason Weimar"

# Composite Types- These are collections composed of the above primitive types.

# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain muxed data types.

dog = ("Rusty", "Brown Dog", 7, False)
print(dog[0])  # output: Rusty
# dog[1] = (
#     "Street Dog"  # Error: cannot be modified ('tuple' obhect does not support item assignment)
# )

#  List - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.

empty_list = []
ninjas = ["Jason", "Rusty", "Michelle"]
print(ninjas[2])
ninjas.append("Pete")
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.

empty_dict = {}
new_person = {"name": "Jason", "age": 37, "weight": 160.2, "has_glasses": True}
print(new_person)
new_person["name"] = (
    "JSON"  # updates if the key exists, adds a key-value pair if it doesn't
)
new_person["hobbies"] = ["MTB", "Photography"]
print(new_person)
w = new_person.pop("weight")  # Removes the specified key and returns the value.
print(w)
print(new_person)

# Common Functions - If we're ever unsure of a value or variable's data type, we can use the 'type' function to find out:

print(type(2.63))
print(type(new_person))

# For data types that have a length attribuute (e.g. lists, dictionaries, tuples,strings), we can use the 'len' function to get the length:

print(len(new_person))  # output: 4 (the number of key-value pairs)
print(len("Coding Dojo"))  # output: 11
