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

print(len{s)

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
dir(something)

print(something.count('t')) # count the number of 't' present
print(something.find('plete')) # find the position of 'plete'
print(something.split('e')) # splits after letter 'e'

thing2 = something.replace('Different', 'Silly')  
print(thing2) #  replace the words

#  something[0] = 'B' gives an error since strings are immutable 


#EXERCISE 7 - ALIASING

#Q1 - create alias and try changing original variable and alias



#Q2 - alias with a string



#Q3 - force a 'deep' copy






