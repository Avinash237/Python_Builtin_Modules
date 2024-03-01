import array

"""
# creating aaray

numbers = array.array('i',[1,3,5,7])
print(numbers)
--------------------------------------------------------------

# typecode

# this attribute returns the typecode of the array
numbers = array.array('i',[1,3,5,7])
print(numbers.typecode)
--------------------------------------------------------------

# itemsize

# The attribute returns the size of the array in bytes
numbers = array.array('i', [1,3,5,7])
print(numbers.itemsize)

--------------------------------------------------------------

# array.append(x)

numbers = array.array('i',[1,3,5,7])
print(numbers)
numbers.append(8)
print(numbers)  # it will append at last index
--------------------------------------------------------------

# array.buffer_info()

-   The method returns a tuple containing the current memory address and the length of 
    the buffer used to retain the contents of the array in elements

numbers = array.array('i', [1,3,5,7])
print(numbers.buffer_info())
--------------------------------------------------------------


# array.byteswap()

-   The method does the byte swap operation on every element of the array. It has no return value

numbers = array.array('i', [1, 3, 5])
print(numbers)
numbers.byteswap()
print(numbers)

--------------------------------------------------------------

# array.count(x)

numbers = array.array('i', [1,3,5,7,1])
print(numbers.count(1))  # 1 present in array 2 times

-----------------------------------------------------------------


# array.extend(iterable)

numbers = array.array('i', [1,3,5,7, 1])
print(numbers)
numbers.extend([2, 4, 8, 10])
print(numbers)


-------------------------------------------------------------------------
"""
# array.insert(i, x)

numbers = array.array('i', [1, 3, 5, 7, 1, 2])
numbers.insert(2, 12)
print(numbers)
