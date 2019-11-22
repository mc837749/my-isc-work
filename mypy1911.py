###
#Chapter 1: Introduction to Python
###
# EXERICE 1 - VARIABLES AND TYPES
#Q1 - creating variables
course = 'python'
rating = 15
print(course)
print(rating)
#Q2 - Use Pythagoras theorem (use **0.5 instead of sqrt function)
b = 2
c = 3

a = (b*2 + c*2)**0.5
print(a)

#Q3 - date types
print(type(a)) # a is different from b and c as it is not an integer
print(type(b))
print(type(c))

#Q4 - convert between data types

print(int(a))
print(type(a))

print(str(a) + 'squared equals' + str(b) + 'squared +' + str(c) + ' squared.')

# EXERCISE 2 - CONTROL FLOW

#Q1 - while loops

#while 1:
#    x = 1

while 0:
    pass

#Q2 - create list for 'for' statements

gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0

while count < 4:
    item = gases[count] #assign each value in 'gases' to a temporary vale 'item'
    print(item,count)
    count+=1

#Q3 - 'if/elif/else' statements

name = 'Lisa'

if name == 'Lisa':
    print(name, 'plays saxophone') # writing name will state it in the output
elif name == 'Bart':
    print(name, 'rides skateboard')
else:
    print(name, 'lives in Springfield')

#Q4 - test for 'truth'

x = 1 
#testing for different values for x
if x:
    print(x,'is True')

if x == 22.1:
    print(x,'is True')

if x == 'hello':
    print(x,'is True')

if x == 22.1:
    print(x,'is True')

if x == 0:
    print(x,'is True')

if x ==0.0:
    print(x,'is True')

if x =="":
    print(x,'is True')

if x == 'False':
    print(x,'is True')

if x == []:
    print(x,'is True')

if x == {}:
    print(x,'is True')

if x == ():
    print(x,'is True')
#Remember zero and empty objects are not considered true!

# EXERCISE 3 - LISTS AND SLICING

x = [1, 2, 3, 4, 5]

print(x[1]) #second item in list

print(x[-2]) #or x(3) for fourth item in list

print(x[0:4]) #slice whole list

print(x[1:4]) #slice 2nd to 4th element

#Q2 - create list from range

y = list(range(1,11))
print(y)
y[0] = 10
print(y)
y.append(11)
print(y)
y.extend([12, 13, 14])
print(y)

#Q3 - combine lists and loops

#empty lists
forward = [] 
backward = []

#updating the lists
values = ['a', 'b', 'c']
for item in values:
    forward.append(item)
    backward.insert(0,item)

print('Forward is', forward)
print('Backward is', backward)

#reversing the oreder of the 'forward'
forward.reverse() #or forward = forward[::-if 1]

print(forward == backward)

#Q4 - using properties oF lists
    
countries = ['uk', 'usa', 'uk', 'uae']
type(countries)
#dir(countries)
#help(countries.count)

countries.count('uk') #counting the countries

while countries:
    #remove the last object in the list and it will loop over all the items in the list
    countries.pop()
    print(countries)
# b = sorted(a) - alphabetically sorted

# EXERCISE 4 - TUPLES

#Q1 - creating tuples


#  create tuple with one value
t = (1,)
#  print the last value in tuple
print(t[-1])

r = range(100, 201)
print(tuple(r))

print(r[0])
print(r[-1])

#Q2 - Enumerate function
mylist = (23, 'hi', 2.4e-10)

#  enumerate will give the position of each item in the tuple
for (count,item) in enumerate(mylist):
    print(count, item)

#Q3 - unpack multiple values in tuple

#  assign a varaible for each of the item in the tuple
(first, middle, last) = mylist
print(first, middle, last)

#  change the variable name
(first, middle, last) = (middle, last, first)

print(first, middle, last)


# EXERCISE 5 - INPUT AND OUTPUT

#Q1 - read CSV file

#opening and reading the file within the working directory
with open('weather.csv', 'r') as reader:
    data = reader.read()
print(data)

#Q2 - read the file line by line

#  while loop reading lines in file until empty string
with open('weather.csv', 'r') as reader:
    while True:
        line = reader.readline()
        if not line: 
            break
        print(line)
print('It\'s over')


#Q3 - use 'for' loop instead of 'while' loop

# reading the line in the file
with open('weather.csv', 'r') as reader:
    header = reader.readline()
    #  creating an empty list
    rain = [] 
    #  extract rainfall values from file and add to 'rain'
    for line in reader.readlines():
        # line.strip() strips white spaces before and after in lines
        # line.split(',')[-1] split the data by comma(',') and select the last value in the list
        # float() remains the data as a non-integer
      
        rainfall  = float(line.strip().split(',')[-1])
        # update the 'rain' list with the values collected in rainfall
        rain.append(rainfall)

print(rain)

#  add the rainfall data into a text file 'myrain.txt'
with open('myrain.txt', 'w') as writer:
    for rainfall in rain:
        writer.write(str(rainfall) + '\n')
#  check the content of the file
with open('myrain.txt', 'r') as reader:
    data_rain = reader.read()
print(data_rain)

#EXERCISE 5 - STRINGS

#Q1 - loop through a string as a sequence

#  create string
s = ('I love to write Python')

#  loop through to display each value in string
for i in s:
    print(i)

#  print 5th value of the string

print(s[4])

#  print last element of s

print(s[-1])

#  print length of s

print(len(s))

print(s[0])
print(s[0][0]) 
print(s[0][0][0])


#Q2 - splitting strings

# split the phrase of 's'
split_s = s.split()
print(split_s)

#  loop through the words and state in which word contains 'i'
for word in split_s:
    if word.lower().find('i') > -1:
        print(f"I found 'i' in {word}")

# if 'i' word:
    # print(f"I found 'i' in {word})

#Q3 - other aspects of strings


something = ('Completely Different')
#dir(something)

print(something.count('t')) # count the number of 't' present
print(something.find('plete')) # find the position of 'plete'
print(something.split('e')) # splits after letter 'e'

thing2 = something.replace('Different', 'Silly')  
print(thing2) #  replace the words

#  something[0] = 'B' gives an error since strings are immutable 


#EXERCISE 7 - ALIASING

#Q1 - create alias and try changing original variable and alias

a = list(range(3))
b = a
print(a, b)

b[0] = 'hello'
print(a, b)

a.append(3)
print(a, b)

#Q2 - alias with a string

a = 'can I change'
b = a
print(a, b)

b = 'different'
print(a, b)

#Q3 - force a 'deep' copy

import copy
a = list(range(3))
b = copy.deepcopy(a)
print(a, b)

b[0] = 'hello'
print(a, b)


# EXERCISE 8 - FUNCTIONS

#Q1 - create simple function

def double_it(number):
    return 2 * number

double_it(2)
double_it(0.5)
double_it('hello')

#Q2 - calculate length of hypotenuse
#  define a funtion with two arguments 
def calc_hypo(a, b):
    #  using the arguments to solve
    hypo = (a**2 + b**2)**0.5
    return hypo

print(calc_hypo(3, 4))

#Q3 - improve function by adding check codes

def calc_hypo(a, b):
    #  check for the type of 'a' and 'b' to be an integer or a float
    if type(a) not in (int, float) or type(b) not in (int, float):
        print('Incorrect type of argument!')
        return False
    #  ensure the value of 'a' and 'b' are positpyive
    if a <= 0 or b <= 0:
        print('Negative argument!')
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo

print(calc_hypo(0, -2))
print(calc_hypo(3, 4))
print(calc_hypo('python', 'java'))

# EXERCISE 9 - SCRIPTS AND LIBRARIES

#Q1 - create python library

#  Create a directory (Linux) called 'dancing'
#  Create a file in 'dacing called '__init__.py' and add a variable
#  Run by using == python -c 'import dancing'

#Q2 - create python module

#  We have a dancer.py file with 'boogie' function which is placed in the 'dancing' file.
#  Import the boogie function == 'python -c 'from dancing.dance import boogie''

#Q3 -

#  Create a new file called dancer.py with the following content:
#   import sys
#   from dancing.dance import boogie
#   moves = sys.argv[1:] = MP: moves is NOT the variable from 'dance.py'
#   boogie(moves)
#  run by using == python dancer.py
#  add values to the 'moves' variable or add the values to the end of the command and run again using == python dancer.py Twist LightBulb

# EXERCISE 10 - SETS AND DICTIONARIES

#Q1 - create sets

a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])

a|b # a.union(b)
a&b # a.intersection(b)

#Q2 -  use a dictionary to count

band = ['mel', 'geri', 'victoria', 'mel', 'emma']

counts = {} #  create an empty dictionary

''' Count the number of the same name appearing in the list 'band' using a dictionary '''

#  loops through each name in the list 'band' and count the number of the same name
for name in band:
    # if there is no existent name in the set 'counts' then give the 		value of the name as 1
    if name not in counts:
        counts[name] = 1
    # if there is an existent name in the set 'counts' then add 1 to 		the value
    else:
        counts[name] += 1

#  
for name in counts:
    print(name, counts[name])


#Q3 - characteristics of dictionaries

if {}: print('hi') #doesn't work

d = {'maggie': 'uk', 'ronnie': 'usa'}

#dir(d) will show the properties of dictionary 'd'

d.items() #  view items in the dictionary
d.keys() #  view the keys in the dictionary
d.values() #  view the values in the dictionary

d.get('isaiah', 'uk') # set default value no matter the key but does not add the key into the dictionary
res = d.setdefault('isaiah', 'uk') # add key and value to the dictionary 'd'

print(res, d['isaiah'])


# EXERCISE 11 - OBJECT ORIENTED PROGRAMMING



# ERRORS, EXCEPTIONS, LOGGING AND DEBUGGING



###
#Chapter 2: NumPy
###


# EXERCISE 1 - ARRAYS 

#Q1
import numpy as np

x = np.arange(1,11)
a1 = np.array(x, dtype = np.int32)
a2 = np.array(x, dtype = np.float32)

print( a1.dtype )
print( a2.dtype )

#Q2

array1 = np.zeros( [2, 3, 4] ) # create arrays with zeros
array2 = np.ones( [2, 3, 4] ) # creates arrays with ones
array3 = np.arange( 100 ) # create arrays with a range

#Q3

a = np.array( [2, 3.2, 5.5, -6.4, -2.2, 2.4] )
print( a[1] )
print( a[1:4] )

a = np.array( [ [2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2.1] ])

print( a[:,3] )
print( a[1:4, 0:4] )
print( a[1:,2] )



# EXERCISE 2 - INTERROGATING AND MANIPULATING ARRAYS

import numpy as np
#Q1

arr = np.array( [ [np.arange(4)], [np.arange(10,14)] ])
print( np.shape(arr) ) # view shape
print( np.size(arr) ) # view size of array
print( np.max(arr) ) # view maximum value in array
print( np.min(arr) ) # view minimum value in array

#Q2

print( np.reshape(arr, (2,2) ) ) # reshape array
print( np.transpose(arr) ) # transpose the array
print( np.ravel(arr) ) # flatten the array to 2-D
print( arr.astype(np.float32) ) # convert to floats


# EXERCISE 3 - ARRAY CALCULATIONS AND OPERATIONS

import numpy as np

#Q1 

a = np.array( [ [ np.arange(4) ], [ np.arange(10, 14) ] ] )

b = np.array( [2, -1, 1, 0] )

a * b # this is allowed in Python

b1 = b*100
b2 = b*100.0

print(b1, b2)

b1 == b2 # True

print(b1.dtype, b2.dtype) # different types (int32 and float32)

#Q2

arr = np.array( [np.arange(10)] )

print( arr < 3 ) #  test if the values are less than 3
print( np.less( arr < 3 ) ) 

condition = np.logical_or(arr < 3, arr > 8)
new_arr = np.where( condition, arr * 5, arr * -5 )
print(new_arr)

#Q3

''' A function takes a 2-D array of horizontal zonal and meridonal wind components, 'u' and 'v' respectivly, and returns an array of the magnitudes of the total wind (sqrt(u**2 + v**2)). 

Test:= if it is less than 0.1, then set it equal to 0.1.

'''

def total_wind_Magnitude(u, v, minmag = 0.1):
    mag = ( u**2 + v**2 )**0.5
    output = np.where( mag > minmag, mag, minmag )
    return output

#test the function out with different arrays
u = np.array([ [4, 5, 6], [2, 3, 4] ])
v = np.array([ [2, 2, 2], [1, 1, 1] ])
print(total_wind_Magnitide(u,v))


u = np.array([ [4, 5, 0.01], [2, 3, 4] ])
v = np.array([ [2, 2, 0.03], [1, 1, 1] ])
print(total_wind_Magnitude(u,v))

# EXERCISE 4 - WORKING WITH MISSING VALUES

import numpy.ma as MA

# create a masked array and mask values in the array manualy and using 'masked_where' 
marr = MA.masked_array(range(10), fill_value = -999)
print(marr, marr.fill_value)

marr[2] = MA.masked
print(marr, marr.mask)

narr = MA.masked_where(marr > 6, marr)
print(narr)
print(narr.fill_value)

# in order to replace the missing value with the fill_value, you create a variable

filled_narr = MA.filled(narr)
print(filled_narr)
type(filled_narr) #<class 'numpy.ndarray'>

#Q2

m1 = MA.masked_array(range(1,9))
print(m1)

m2 = m1.reshape(2,4)
print(m2)

m3 = MA.masked_where(m2 > 6, m2)
print(m3)

print(m3*100)

# use np to generate an array of ones
result = m3 - np.ones((2,4))
print(result)
print(type(result)) # <class 'numpy.ma.core.MaskedArray'>


###
# Chapter 3 - Matplotlib
###

# EXERCISE 1 - 

import matplotlib.pyplot as plt
#Q1

plt.plot(range(10))
plt.show()

#Q2

Time = list(range(7))
CO2_conc = [250, 265, 272, 260, 300, 320, 389]
plt.plot(Time, CO2_conc, 'b--')
plt.title ('The evolution of CO2 concentration')
plt.ylabel('CO2 Concentration (ppm)')
plt.xlabel('Time (decades)')
plt.show()

Temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(Time, CO2_conc, 'b--'. Time, Temp, 'g-')
plt.savefig('co2_temp.pdf')
plt.show()

# EXERCISE 2 - 

#Q1

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
ax1.plot(Time, CO2_conc)
ax1.set_ylabel('CO2 concentration')
ax2 = ax1.twinx()
ax2.plot(Time, Temp, 'r-')
ax2.set_ylabel('Temperature')
plot.show()

#Q2

plot.subplot(1, 3, 1)
x = range(0, 10, 1)
plt.plot(x)

plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plot(y)

plt.subplot(1, 3, 3)
z = [4]*10
plt.plot(z)
plt.show()


#Q3

from example_code.map_data import *
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


fig = plt.figure()
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
m.drawcoastlines()

iml = m.pcolormesh(lons,lats,tas, shading='flat', cmap=plt.cm.jet,latlon=True)

plt.savefig('tas1.png')
plt.show()

fig.figure()
plt.title('Change in Surface Air Temperature from MOHC HadGEM2-ES')
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

m.drawcoastlines()
m.drawparallels(np.arange(-90.,99.,30.))
m.drawmeridians(np.arange(-180.,180.,60.))
iml = m.pcolormesh(lons,lats,tas, shading='flat', cmap=plt.cm.jet,latlon=True)
cb = m.colorbar(iml, 'bottom', size='5%', pad='2%')

plt.savefig(tas2.png)
plt.show()
















































