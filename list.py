# play around with the drawers!

drawers = ["documents", "envelopes", "pens"]

# Print the second value from the list (envelopes)
print(drawers[1])

# Change "pens" to "useless manuals"
drawers[2] = "useless manuals"
print(drawers)

# Change the first value to whatever is the second value
drawers[0] = drawers[1]
print(drawers)

# Adding (appending) to a list
drawers.append([4747, "Jason"])
print(drawers)

# Slicing

words = ["start", "going", "till", "the", "end"]

# Sub-ranges (portions) of the list

print(words[1:])  # prints ['going', 'till' , 'the' , 'end']
print(words[:4])  # prints ['start', 'going', 'till', 'the']
print(words[2:4])  # prints ['till', 'the']

# Making a copy of a list

copy_of_words = words[:]
print(copy_of_words)

copy_of_words.append("dojo")  # only appends to the copy

print(copy_of_words)  # prints ['start', 'going', 'till', 'the' , 'end', "dojo']
print(words)  # prints ['start', 'going', 'till', 'the', 'end' ]

# Built-in Functions for Lists

my_list = [1, "Jason", "hi"]
print(len(my_list))
# output = 3

number_list = [1, 2, 3, 4, 5]
print(max(number_list))
# output = 5
print(min(number_list))
# output = 1
number_list_2 = [1, 4, 3, 7, 8, 10, 77, 76, 90, 100]
print(sorted(number_list_2))
# output = [1, 3, 4, 7, 8, 10, 76, 77, 90, 100]

# List-Specific Methods: The .append method is an ex of a built-in list method. Like string methods, in order to use a built-in list method, you must use dot-notation with an existing list.

some_list = ["Downhill", "Photography", "Guitar"]

some_list.append("37")
print(some_list)
# output = ['Downhill', 'Photography', 'Guitar', '37']

some_list.pop()
print(some_list)
# output = ['Downhill', 'Photography', 'Guitar']

# Some commonly used list methods:

"""
• list.append (value) 
appends a value to the end of the list.

• list.pop(index)
remove a value at given position. if no parameter is passed, it will remove
the last value in the list.

• list.index(value)
returns the index (position) of the given value if it exists in the list and
raises an error if it does not exist.

• list.reverse()
reverses the order of the elements, in place *

• list.sort()
sorts the items in order of least to greatest, or alphabetically for strings, in place *

--- 'in place' means it changes that same array, instead of returning a new array. ---
"""

# Conditional Statements: if, elif, else

x = 12
if x > 50:
    print("larger than 50")
else:
    print("smaller than 50")

x = 55
if x > 10:
    print("larger than 10")
elif x > 50:
    print("larger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we eill only see 'larger than 10'.

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false


"""
Operator:
    == : Checks if the value of two operands are equal. (ex. 1==2 => False, 1==1 => True)
    != : Checks if the value of two operands are not equal. (ex. 1!=2 => True, 1!=1 => False)
    > : Greater Than
    < : Less Than
    >= : Greater or Equal to
    <= : Less Than or Equal to
    and : Checks that each expression on the left and right are both True
    or : Checks if either the expression on the left or right is True
    not : Reverses the true-false value of the operand (ex. - not true => False, - not False => True, - not1>=2 => True, - not1<=2 => False, - not(1<=2 and 2>=3) => True, - not1<=2 and 2>=3 => False)
"""
