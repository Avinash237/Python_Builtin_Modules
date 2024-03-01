import random
"""
print(random.random)

-   The random.random() method returns a random float number between 0.0 to 1.0. 
    The function doesn't need any arguments.
-------------------------------------------------------------------------

# random.randint()
# Generate Random Integers
print(random.randint(1,100))

it will genertae random integer between 1 - 100
----------------------------------------------------------------------------


# random.randrange()
# Generate Random Numbers within Range

print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))

----------------------------------------------------------------------------

# random.choice()
# Select Random Elements
print(random.choice('computer'))
print(random.choice([12,23,45,67,65,43]))
----------------------------------------------------------------------------
"""

# random.shuffle()
# Shuffle Elements Randomly

numbers=[12,23,45,67,65,43]

random.shuffle(numbers)
print(numbers)

random.shuffle(numbers)
print(numbers)