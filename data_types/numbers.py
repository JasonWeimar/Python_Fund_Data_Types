# Conversion - All Python objects have data type methods we can use to convert nymber types from one to another.

int_to_float = float(35)
print(int_to_float)

float_to_int = int(44.2)
print(float_to_int)

int_to_complex = complex(35)
print(int_to_complex)

print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# Random Number - Python does not have a built in random number generator, use the 'random module' instead.

import random

print(random.randint(2, 5))  # privides a random number between 2 and 5
