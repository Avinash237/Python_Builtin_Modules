import time
"""
# time()
seconds = time .time()
print('Seconds since epoch =', seconds)

-   time() method print current time seconds
----------------------------------------------------------------

# time.ctime()
local_time = time.ctime()
print(local_time)

# time.ctime() will print current time with day and year

------------------------------------------------------------------------------

# time.sleep()

time.sleep() suspends a program’s execution for a specified number of seconds

print('Welcome to time trivel')
time.sleep(3)
print('after 3 seconds...')
--------------------------------------------------------------------------------


# time.mktime()

import time

t = (2021, 10, 21, 6, 52, 30, 4, 294, 0)

local_time = time.mktime(t)
print('Local time:', local_time)

-   The inverse of the time.localtime() method is time.mktime(). 
    It accepts the struct time (all the struct time tuples) as an argument and returns the 
    time in seconds that has elapsed/passed since the epoch.

--------------------------------------------------------------------------------
"""

