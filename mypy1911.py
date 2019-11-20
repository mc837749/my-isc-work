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
dir(countries)
help(countries.count)

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

#Q1










