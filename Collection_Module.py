from collections import *
#from collections import Counter
"""
# Counter

A = 'Python_DataScience'

result = Counter(A)
print(result)

- counter method will print out of each letter store in A 
-    along with how many times that letters appears

-------------------------------------------------------------------------------------
# values() function

-   The values() function will give a list of the counts associated with all the values.

a=["apple","mango","cherry","apple","mango","mango"]
result=Counter(a)
print(result)
print(result.values())

---------------------------------------------------------------------------------------

# namedtuple() function
person=namedtuple("person",["name","place","sex","age"])
id=person("kavya","Hyderabad","F","21")
print(id[1])
print(id[3])
print(id.place)
print(id.age)

The namedtuple() will allow us to create tuples with named fields.
So, instead of accessing the items using the indices, 
we can access them using the dot notation.
-------------------------------------------------------------------------
# OrderedDict

d=OrderedDict()
d['sachin']=100
d['dhruv']=116
d['Dhoni']=90
d['Rohit']=110
d['Kohli']=95
print(d)

OrderedDict is a dictionary which can remember the order of its items. 
It is used for preserving the order in which the items will be added into the list.
------------------------------------------------------------------------------------------
# defaultdict

The defaultdict has all the functionalities of a dictionary with the additional feature where it will never give a KeyError. 
In a dictionary, if you try to access or modify the keys that do not exist, you will get a KeyError.
Whereas, defaultdict always assigns a default value if the key does not exist. Hence, defaultdict is used for handling missing keys.

d=defaultdict(int)
d['Sachin']=90
d['Dhoni']=80
d['Virat']=95
print(d)
print(d['Dhoni'])
print(d['Rohit'])  # will assign 0 parameter given int
print(d['druv'])  # will assign 0 

-   default value will be 0
--------------------------------------------------------------------------------------------

# deque()

# The Python deque() is a double-ended queue which allows us to add and remove elements
# from both the ends
list = ["x","y","z"]
deq = deque(list)
print(deq)
# insertion
deq.append("p")
deq.appendleft(('l'))
print(deq)

# removal

deq.pop()
deq.popleft()
print(deq)
----------------------------------------------------------------------------------------


# ChainMap

ChainMap combines a lot of dictionaries together and returns a list of dictionaries. 
ChainMaps basically encapsulates a lot of dictionaries into one single unit with no restriction 
on the number of dictionaries.

import collections
dictionary1 = { 'a' : 1, 'b' : 2 }
dictionary2 = { 'c' : 3, 'b' : 4 }
chain_Map = collections.ChainMap(dictionary1, dictionary2)
print(chain_Map.maps) 
------------------------------------------------------------------------------------------
"""