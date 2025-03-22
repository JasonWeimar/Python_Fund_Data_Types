# --- Lists ---

# In Python, arrays are called lists.
# Lists are ordered and changeable.
# Lists allow duplicate vallues.

#  List Createion:
colors = ["Red", "Green", "Blue", "Yellow"]

# List indices:
"""
Lists have indices just like arrays have indices in JavaScript. They are also zero-indexed.
"""
print(colors[1])

"""
Python supports negative indices. A -1 index will refer to the last element in a list.
"""
print(colors[-1])
print(colors[-2])
# print(colors[-5]) error index out of range

# Common Methods:

"""
Length:
    Pass a list to the len() method to return the number of elements in lest

Append:
    append() - adds an element to the end of a list.
    remove() - removes the specified element from a list.
    pop() - removes the element at the specified position.
"""

colors.append("Coral")
print(colors)

colors.insert(1, "Gold")
print(colors)

colors.remove("Green")
print(colors)

print("Before: ", colors)
last_item = colors.pop()
print("After: ", colors)

print(last_item)

colors.pop(0)
print(colors)


# Sort, Reverse:

"""
The sort() method sorts a list in ascending order in-place.
The reverse() method reveses a list.
"""

fibonacci = [1, 1, 2, 0, 5, 8, 13, 3]

fibonacci.sort()
print(fibonacci)

fibonacci.reverse()
print(fibonacci)

"""
Sort & Reverse returns 'none' - But everything prior to calling the method mutates the actual array that you call Sort/Reverse on ('in-place')
"""

#  More list methods: https://www.w3schools.com/python/python_ref_list.asp


"""
Tuples:
    A Tuple is a collection which is ordered and unchangeable.
    Tuples allow duplicate values.
    Tuples are written with round brackets (parenthesees).
"""

# Tuple Creation:

colors = ("Blue", "Blue", "Purple", "Coral")
print(type(colors))

#  Tuples are zero-indexed.
print(colors[2])

"""
A practicle use for Tuples would be to queuery results from a data-base... In this scenario, you would never want the results to change. 
"""


# Conditionals:

"""
Used to make decisions, based on certain conditions.

if conditions: Code to execute if condition isi True.

elif condition: Code to execute if condition1 is False and condition2 is True. (When setting these up, list the most stringent condition at the top.) - (can have as many elif's as you want)

else: Code to execute if condition is False. ('otherwise do this')
"""

num = 15

if num > 10:
    print(f"{num} is greater than 10")
elif num > 3:
    print(f"{num} is greater than 3")
else:
    print(f"{num} is not greater than 10 or 3")


# --- EXERCISE ---

"""
Enter a number: 5
5 is a positive number.

Enter a number: -3
-3 is a negative number.

Enter a number: 0
0 is neither positive nor negative.
"""

user_num = int(input("Enter a number:"))
print("You chose ", user_num)

if user_num < 0:
    print(f"{user_num} is a negative number.")
elif user_num > 0:
    print(f"{user_num} is a positive number")
else:
    print(f"{user_num} is neither positive nor negative")


# --- Loops & Functions start in W1D3 Office Hour ---
