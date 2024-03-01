from itertools import *

"""

# count(start, stop)

for i in itertools.count(10,5):
    if i == 50:
        break
    else:
        print(i,end=" ")
-   It prints from the start value to infinite. The step argument is optional, 
    if the value is provided to the step then the number of steps will be skipped        
 ----------------------------------------------------------------------------------       

# cycle(iterable)

temp = 0
for i in itertools.cycle("123"):
    if temp > 7:
        break
    else:
        print(i,end=' ')
        temp = temp+1  
        
-   This iterator prints all value in sequence from the passed argument. 
    It prints the values in a cyclic manner
----------------------------------------------------------------------------------       

# repeat(val,num)

print("Printing the number repeadtly:")
print(list(itertools.repeat(40,15)))
----------------------------------------------------------------------------------


# Product()

print("We are computing cartesian product using repeat Keyword Argument:")
print(list(product([1, 2], repeat=2)))
print()

print("We are computing cartesian product of the containers:")
print(list(product(['Python', 'case', 'fail'], '5')))
print()

print("We are computing product of the containers:")
print(list(product('CD', [4, 5])))


-   It is used to calculate the cartesian product of input iterable. 
    In this function, we use the optional repeat keyword argument for computation of the
    product of an iterable with itself. The repeat keyword represents the number of repetitions.
    It returns output in the form of sorted tuples.

----------------------------------------------------------------------------------


# Permutations()

print("Computing all permutation of the following list")
print(list(permutations([3, "Python"], 2)))
print()

print("Permutations of following string")
print(list(permutations('AB')))
print()

print("Permutation of the given container is:")
print(list(permutations(range(4), 2)))

-   It is used to generate all possible permutation of an iterable. 
    The uniqueness of each element depends upon their position instead of values. 
    It accepts two argument iterable and group_size. If the value of group_size is none or 
    not specified then group_size turns into length of the iterable.

----------------------------------------------------------------------------------
"""


