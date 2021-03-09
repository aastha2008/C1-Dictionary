'''
03/08/2021

Review

List
mutable

List functions

  LIST.insert(INDEX,ELEMENT)
  LIST.append(ELEMENT)
  LIST.remove(ELEMENT)
  LIST.pop(INDEX)

LIST[INDEX]=ELEMENT


Tuple
immutable, ()



Dictionary 
Another type of list, stores data/values inside the curly brackets {}
Similarly to a list, it's mutable, however the index is a key, which is linked to data/values


student={}
student["name"]="John"
student["age"]=12
student["weight"]="120lbs"
student["school"]="Evergreen"
student["Python"]=True


print(student)
print(student["weight"])
'''


# Exercise 1:
#for loop
'''
*
* *
* * *
* * * *
* * * * *
'''
for x in range(5): #[0,1,2,3,4]
  print("* " * (x+1))

## Exercize 2:
'''
* * * * *
* * * *
* * *
* *
*
'''

print("Ex 2a: ")
for x in range(5,0,-1):
  print ("* " * x)


print("Ex 2b: ")
for y in range(5):   #. [0, 1, 2, 3, 4]
  print ("* " * (5 - y))

## Exercize 3:
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
print("Ex 3a: ")
for z in range(5):     # [0, 1, 2, 3, 4]
  print(" " * (5-z) + "*" * (z +1))

print("Ex 3b: ")
for z in range(5):     # [0, 1, 2, 3, 4]
  print(" " * 3 * (4 - z) + "*  " * (z + 1))


## Exercize 4:
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''

print("Ex 4a: ")
for z in range(5):     # [0, 1, 2, 3, 4]
  print(" " * z + "*" * (5-z))


print("Ex 4b: ")
for j in range(5):     # [0, 1, 2, 3, 4]
  print("   " * j + "*  " * (5-j))


'''
** Time
Handles time related tasks

Formula

import time. # Import the time library

Useful Time functions:

1. time.time()
   - Returns floating-point numbers in seconds passed since epoch
     (Jan. 1st 1970, 00:00 UTC)
   - Use it for Date Airthmatic (etc. duration)

2. time.sleep(NUMBER)
   - Suspends (delays) execution/running of the current thread for the given number of seconds
    
'''
import time
print("hello")
print(time.time())

for x in range(10):
  print(str(x) + " seconds has passed")
  time.sleep(1)