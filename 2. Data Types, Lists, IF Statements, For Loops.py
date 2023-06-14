# -----------------------------------------------------------------------------
#%%# Q1 FUNDAMENTAL DATA TYPES
#%% --- a) None Type 
'''
None is not the same as 0, or False or an empty string “”. None is a datatype 
of type NoneType. Check for yourself by running below commands (i.e. printing 
out the type of each object: None, 0, False, ""): 
'''
print(type(None)) # it has a type of its own
print(type(0)) 
print(type(False)) 
print(type(""))

'''
Now create a variable x = 5 and check if type of x is equal to type of None. 
Hint: equality operator.
'''

x = 5
type(x) == type(None) # False
type(x)

#%% --- b) Numeric Types
'''
Examine the type of variable created when initialising y1 = 15.0 vs when using 
brackets y2 = (15.0). Did you create a float and a tuple or was it a float in 
both cases? Understand why.
'''
y1 = 15.0 
y2 = (15.0) 
# Check each variable's data type
type(y1)
type(y2)
# Both are floats. Using round brackets is just a long way of creating a float.
# If we wanted a tuple, we should say y2 = (15.0,) as the trailing comma is 
# needed after a single element.

'''
Try again when using a boolean True, i.e. b1 = True and b2 = (True). Did you 
create a bool and a tuple or was it bool type in both cases? Understand why.
'''
b1 = True
b2 = (True)

# Note above is meant to demonstrate that using brackets is an equivalent, but 
# longer, way of creating scalar types. 

#%% --- c) Sequences
'''
Create your own example variables for each sequence type (string, tuple, list). 
Ensure that your containers (tuple, list) store inside as elements all of the 
data types allowed for that container. For example: tuple allows elements of 
any type, e.g.: 
T1 = (1, {}, [1,2]) 
contains 3 elements: int 1, empty dictionary {} and list with two elems [1, 2]. 
'''
# your string example
s = "Object-Oriented Programming"

# your tuple example
T = (None, 100, True, 15.6, "Hello", (1,2,3), [1,2,3], frozenset({1,2,3}), {1,2,3}, {"A":1, "B":2})
# equivalently:
T = None, 100, True, 15.6, "Hello", (1,2,3), [1,2,3], frozenset({1,2,3}), {1,2,3}, {"A":1, "B":2} 

# your list example
L = [None, 100, True, 15.6, "Hello", (1,2,3), [1,2,3], frozenset({1,2,3}), {1,2,3}, {"A":1, "B":2}]

'''
Next investigate the following: 
i. Put integers inside a string. What happens to them? i.e. are they still 
   integers or do they become a string?
'''
s = "123"
type(s) # anything placed inside the quotation marks becomes a string.

'''
ii.	List is commonly used to store data. If you did not want your data set to 
    be altered which sequence type would you use instead?
'''
# You would use a tuple. This is an immutable equivalent to the list. 
# Attempting to change value of a tuple will generate an error, e.g.:
T[0] = 15   
# TypeError: 'tuple' object does not support item assignment

'''
iii. Create a new variable T2 = 1, {}, [1,2]. This also creates a tuple just 
as you did above T1 = (1, {}, [1,2]) i.e. creating tuples does not require 
round brackets. 
'''
T2 = 1, {}, [1,2]
type(T2) # this is still a tuple even though round brackets were not used.

# Another example: create variables and check their type. Which one is a tuple?
T3 = 1, # this is a tuple: we do not require round brackets, and there is a 
# trailing comma which specifies this is a tuple with a single element.
T4 = 1
type(T3)
type(T4)

# Note: this is not the case for lists. You must use square brackets, i.e. 
# you are not allowed to drop the sq brackets
L = [1, 2, 3] # this is a list
type(L)

'''
iv.	What type do you expect to observe if you execute myList = 1, 2, 3? 
'''
myList = 1, 2, 3 # this is a tuple. Now we have a misleading variable name.
type(myList)

#%% --- 1d) Sets and String Methods
# https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset
'''
i. Create a set variable containing numeric, string and tuple objects.
Next attempt to create another set which also contains a list. 
Why were you not able to do so? 
(Hint: see Slide on Fundamental Data Types, column called “meaning/use”).
'''
S = {'abc', 1, 1.0, (1,2,3)} # all elements are allowed (immutable type)
S = {'abc', 1, 1.0, (1,2,3), [1,2,3]} # TypeError: unhashable type: 'list'

# If you attempted to place a list inside a set, it would not work. 
# Reminder this is because sets only allow elems of immutable type. 
# This is because of the way items are looked up inside a set.
# E.g. try:
S = {[1,2,3]}

'''
ii.	Initialise a list L = [1, 1, 1, 2, 3]. Typecast this list to a set using 
    operation set(L). Which list elements feature in your new set? Why were 
    some elements of the list dropped? 
'''
L = [1, 1, 1, 2, 3]
S = set(L)
print(S) # {1, 2, 3} Non repeating elements only.
# Remember that sets are unordered collection of elements, so technically the
# print command does not have to result in the ordered 1,2,3 result.

'''
iii. Common uses of set data type in Python include membership testing, 
     removing duplicates from a sequence, and computing standard math 
     operations on sets such as intersection, union, and difference. Let's
     examine these operations using Federal Reserve Statement Analysis.
     
     FIRST READ:
     I) I.	Federal Reserve Statement Background Information in LAB.pdf, 
     then proceed with below qns.
'''
fomc_sep2018 = ["The", "Committee", "expects", "that", "further", "gradual", "increases", "in", "the", "target", "range"]
fomc_dec2018 = ["The", "Committee", "judges", "that", "some", "further", "gradual", "increases", "in", "the", "target", "range"]

'''
What is the type of each variable?
'''
type(fomc_sep2018) 
type(fomc_dec2018) 
# list, contains elements separated by a comma, and square brackets around it

'''
How are the 2 phrases represented inside this variable? i.e. is the sentence 
one long string or are words separated out as elements? 
'''
# phrases are split into words which form elements of each lsit.

'''
Check how many elements are in each container (i.e inside fomc_sep2018 and 
fomc_dec2018). 
Hint: len(obj) to check obj length.
'''
nSep = len(fomc_sep2018)
nDec = len(fomc_dec2018)

'''
Use fomc_sep2018 and fomc_dec2018 to create new variables of type set.  
Hint: You can convert a list L to a set by stating set(L).
'''
A = set(fomc_sep2018)
B = set(fomc_dec2018)

'''
Find union between two sets i.e. all elements (words) occurring in 2 sets.
Hint: Union is performed using | operator e.g. print(A | B)	 or equivalently 
use A.union(B) or other way around B.union(A)
'''
# equivalent ways of checking the union (all elements occuring in 2 sets)
AB_union1 = A | B
AB_union2 = A.union(B) 
AB_union3 = B.union(A) 
print(AB_union1)           
# {'Committee', 'gradual', 'judges', 'that', 'increases', 'the', 'The', 'some', 
# 'expects', 'range', 'in', 'further', 'target'}

'''
Check the intersection between two sets i.e. same words occurring in both sets.
Hint: use  A.intersection(B) command.
'''
# equivalent ways of checking for intersection
AB_intersection1 = A.intersection(B) 
AB_intersection2 = B.intersection(A)
print(AB_intersection1)    
# {'Committee', 'gradual', 'range', 'that', 'increases', 'in', 'the', 
# 'further', 'The', 'target'}

'''
Find which word has NOT been used in Dec phrase. i.e. find set elements which 
only occur in A and not B.
Hint: use A – B or equivalently A.difference(B)
'''
AB_diff1 = A - B
AB_diff2 = A.difference(B)
print(AB_diff1)            # {'expects'}

'''
Find which words are NEW in Dec phrase. i.e. find set elements which only occur 
in B and not A.
Hint: use B – A or equivalently B.difference(A).
'''
BA_diff1 = B - A
BA_diff2 = B.difference(A)
print(BA_diff1)            # {'judges', 'some'}

#%% --- e) Dictionaries
'''
A dictionary is a mapping between a set of objects (unique keys) and a set of 
objects (values). The values that the keys point to can be of any type. Think 
of dictionaries as you would of a regular book: words are ‘keys’ and 
descriptions are ‘values’. You can thus look up a key and extract the 
associated value (explanation or in our case content stored under that key).

Create a dict with 3 months of the year as keys: Jan – Mar and put in numerical 
values 1 - 3 into it corresponding value pair.
'''

months = {"Jan":1, "Feb":2, "Mar":3}
# remember that key:value pairs are separated by a comma

#%% EXTRA  Only complete when finished the main questions.
# f) --- List 
'''
List is a container which is used to store elements of any type inside of it. 
You are allowed to store lists as elements of another inside a list. 
Given the following 3 sales prices data from customers, create another list L,
where each customer forms an eleemnt of that list.
'''
deepmind   = [262.75, 273.26, 271.23, 273.36, 266.38]
openai     = [188.47, 186.30, 187.29, 188.21, 184.70]
neuralink  = [28.18,  27.68,   27.49,  27.93,  27.33]

L = [deepmind, openai, neuralink] # 3 elements separated by commas

# Use command len() to establish the number of elements of the list you created
len(L) # 3
# Note that we have 3 customers and therefore if L is designed correctly should 
# have 3 elements.

# --- g) Set
'''
Let's return to the example where we had a list and were converting it to set.
Note set() function actually changes the data type of variable to a set. Hence
we were able to typecast a list to a set. 

However if you tried to create a set using S = {elem1, elem2, etc} & put a list 
inside, you would get an error. This is because {} operation creates a set from 
the variables specified inside the command. And remember that we are only 
allowed to place immutable types inside a set.
'''
L1 = [1, 1, 1, 2, 3]
# Try this, you will obtain an error
S = {L1}
# However typecasting to a set works, where set() is a function that performs 
# the type change
S = set(L1)


# -----------------------------------------------------------------------------
#%% Q2 OPERATIONS ON SEQUENCES
s = "Covid: How will we know if the vaccine is working?"

L = ['Covid:','How','will','we','know','if','the','vaccine','is','working?']

T = ('Covid:','How','will','we','know','if','the','vaccine','is','working?')

# a) --- Indexing
'''
Indexing extracts a single element from a sequence using square brackets.
Working with one of above varaibles (s, L, T):
    first element
    2nd element
    element at position (approx) half way through 
    last element
'''
s[0]
s[1]
n = len(s) // 2
s[n]
# remember that for strings every character is counted as length 1

# b) --- Slicing
'''
Slicing extracts a subset of the sequence, using tuple T extract the following:
    every 2nd element
    the first half of the data
    the second half of the data
    all element
    reverse the sequence
'''
T[::2]
T[:n]
T[n:]
T[:]
T[::-1]

# c) --- Extended Slicing
'''
EXTRA:
(i) 
    Open up L2_Code.py and find the section on Operations on Sequences. 
    There is a list L with 10 elements. Go over 'minus notation section' and 
    'extended slicing section' (line 79-119).
(ii)
    Go over rest of the exampes for operations on sequences (lines 121 - 148).
'''
# Simply run provided code in L2_Code.py 


# -----------------------------------------------------------------------------
#%% Q3 IF-ELIF-ELSE
# --- a) If Statement
'''
You are working with a boolean varaible, x = False. 
Write an IF statement to check whether x is equal to 0. 
If the condition is true, print out: 0 is treated as False in Python.
'''
x = False
if x == 0:
    print('False is treated as 0 in Python')
# Reminder: 1 is treated as True

# --- b) If-Else Statement
'''
Write an If-ELSE statement which will test whether a number is even or odd, 
assign the result to a boolean variable called isEven. 
Finally print out the isEven variable after you have completed the test.
Use x = 10 and x = 7 to check your code works correctly.
'''
x = 10
if x % 2 == 0:
    isEven = True
else:
    isEven = False
print(isEven)    

'''
EXTRA:
You are learning how to code efficiently. Therefore, try to think of a way, to
solve this problem with shorter code, i.e. which only uses the if statement.
'''
isEven = False
if x % 2 == 0:
    isEven = True
print(isEven) 

# --- c) [EXTRA] Only complete when finished the main questions.
'''
You have the following information on two stocks A and B. 
-	Annual return of each stock (in percent); 
-	Statistical measure of stock’s volatility in relation to the market called 
    beta (this represents the tendency of a security’s returns to respond to 
    swings in the market and thus used as a measure of risk). A beta of 1 means 
    that, when the markets moves up/down by 1% the stock will, on average, also 
    move up/down by 1%. 
'''	
retA = 2.1     # annual return on stock A (in percent)
betaA = 1.7    # annual beta A
retB = 7.2     # annual return on stock B (in percent)
betaB = 0.8    # annual beta B

if retB > retA:
    print("Return of stock B outperformed A")
elif retA == retB:
    print("Returns are equal")
    if betaB < betaA:
        print("Stock B is favoured over stock A")
else:
    print("Return of stock B underformed A")
# Return of stock B outperformed A

# -----------------------------------------------------------------------------
#%% Q4 TYPECASTING
'''
a) Typecast float 16.7 to an integer, check the answer, why is it 16 and not 17 
'''   
x1 = int(16.7) # answer is 16 since int floors the decimal to 0 (rounded down)  
  
'''    
b) Typecast string “100.76” to a float
'''    
x2 = float("100.76") 
  
'''   
c) Typecast a string "Derivative" to a tuple, list, set. Observe the order of 
    the items in the set – this is what we mean by ‘unordered’
'''    
s = "Derivative"
T = tuple(s) # ('d', 'e', 'r', 'i', 'v', 'a', 't', 'i', 'v', 'e')
L = list(s)  # ['d', 'e', 'r', 'i', 'v', 'a', 't', 'i', 'v', 'e']
S = set(s)   # {'a', 'd', 'e', 'i', 'r', 't', 'v'} NON REPEATING MEMBERS ONLY
print(T)
print(L)
print(S)


# -----------------------------------------------------------------------------
#%% Q5 RANGE FUNCTION
'''
We will examine the sequences that range function can generate. Remember that 
typically range produces one number at a time, uses it and discards it, then 
the next number gets generated etc. This is done for memory efficiency and is 
designed to work together with a for loop.

For the above reason range does not create the sequence all at once, rather on 
a one-by-one element basis. In order to observe the sequence we need to 
typecast range to a different data type (e.g. list).
'''
# --- a) First check output of (note this won't reveal the sequence itself):
range(5)
range(0, 5)
range(0, 5, 1)

# Next typecast range(5) to a str, tuple, and a list.
# Which command actually revealed the entire sequence?
# What do the numbers in each position inside range(x1, x2, x3) mean?
str(range(5))   # 'range(0, 5)'
tuple(range(5)) # (0, 1, 2, 3, 4)
list(range(5))  # [0, 1, 2, 3, 4]
# typecasting to tuple or list reveals the entire sequence generated by range

# --- b) 
'''
Give an example of a descending sequence produced by range, ensure to display
the full sequence. 

Produce a descending sequence which starts at 100, stops at 40 and reduces in 
steps of 20. Ensure that you display (print) the entire sequence.
'''
print(list(range(10, 0, -1))) # typecast to a list to observe the sequence.

print(list(range(100, 39, -20))) # [100, 80, 60, 40]
# If try range(100,40,-20) the stop position is auto-incremented to 41

# --- c)
'''
Is it correct to say that elements of a sequence generated by range are 
produced all together at once and are kept in the memory available to be 
re-used on many occasions?
'''
# Incorrect:
# Elements are produced on a need by basis and can only be iterated over once
# They are generated 1-by-1, and get discarded 1-by-1 after they have been used

# --- d)
'''
Examine output of this command print(list(range(-2, -10, -2))) which uses 
negative numbers for start, stop, step. 
-	Is this an ascending or descending sequence? 
-	Why did you not observe -10 inside the generated sequence?
'''
print(list(range(-2, -10, -2))) # [-2, -4, -6, -8] # this is a descending seq
# which stops at -9 (since Python adds +1 to end of descending range seqs)


# -----------------------------------------------------------------------------
#%% Q6 FOR LOOP
# --- a) For loop comprehension question
'''
You have 3 lists containing names, surnames and total holdings (in millions) 
of high net worth individuals investing in your fund. 
'''
names = ["LeBron", "Kyrie", "Damian"] 
surnames = ["James", "Irving", "Lillard"]
holdings = [45.3, 37.5, 31.2]
'''
Your task is to print out the name, surname and their holdings on one line for 
each customer, so that you obtain the following result at the end:
LeBron James 45.3 
Kyrie Irving 37.5
Damian Lillard 31.2
Your task is to do so efficiently, hence you need to use the for loop.

Hint1: you can print several items on the same line by separating them with a 
       comma, e.g. print(a, b, c)
Hint2: remember indexing of elements in a list starts from 0.
'''
numPts = 3 # we use n=3 because there are 3 elements in each list 
for ii in range(numPts): 
    print(names[ii], surnames[ii], holdings[ii])
# LeBron James 45.3
# Kyrie Irving 37.5
# Damian Lillard 31.2


# --- b) Net Present Value 
'''
FIRST READ:
     II) Net Present Value Financial Question in LAB.pdf with the question. 
     Then use a for loop in order to calculate the NPV.
     You should find the answer of 1.145.
'''
cost = 5 # millions (equipment 2.8 + working capital 2.2)

r = 0.15 # discount rate
L = [1.30, 1.42, 1.54, 1.66, 3.98] # cashFlows, year1 = 1.3 etc
numYears = len(L)
# create a list PVs of length len(L) containing zeros (i.e. preallocate memory)
PVs = len(L) * [0] 
for ii in range(numYears):
    yr = ii+1
    PVs[ii] = L[ii] / ((1 + r) ** yr)
npv = sum(PVs) - cost
print(npv) # 1.145 million

# Only complete when finished the main questions.
# --- c) [EXTRA] Applied For Loop Example: Float Point Arithmetic! 
'''
https://0.30000000000000004.com 
Your language isn’t broken, it’s doing floating point math. Computers can only 
natively store integers, so they need some way of representing decimal numbers. 
This representation is not perfectly accurate. This is why, more often than not 
'''
0.1 + 0.2 != 0.3
'''
When you have a base-10 system (like humans), it can only express fractions 
that use a prime factor of the base. The prime factors of 10 are 2 and 5. 
So 1/2, 1/4, 1/5, 1/8, and 1/10 can all be expressed cleanly because the 
denominators all use prime factors of 10. 
In contrast, 1/3, 1/6, 1/7 and 1/9 are all repeating decimals because their 
denominators use a prime factor of 3 or 7.

In binary (or base-2 computer systems), the only prime factor is 2, so you can 
only cleanly express fractions whose denominator has only 2 as a prime factor. 
In binary, 1/2, 1/4, 1/8 would all be expressed cleanly as decimals, 
while 1/5 or 1/10 would be repeating decimals. 
So 0.1 and 0.2 (1/10 and 1/5), while clean decimals in a base-10 system, 
are repeating decimals in the base-2 system the computer uses. 

When you perform math on these repeating decimals, you end up with leftovers 
which carry over when you convert the computer’s base-2 (binary) number into a 
more human-readable base-10 representation.
'''

# Examine 0.1 when you print it out with rounding, or to 20 deicmal places:
print(0.1)
print("%.20f" % 0.1)

'''
Design a for loop which will print out values 0.1 0.2 ... 1.0 to 20 decimal 
places (i.e. your loop will need to iterate 10 times). 
Which decimals are represented exactly? 
'''
L = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# L = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
for ii in range(10):
    print("%.20f" % L[ii])
    # print(L[ii] == L[ii]) # all True

'''
Always worry when testing equality between floats after some arithmetic was
performed. 
'''
# For example, while the following works fine:
0.1 == 0.1       # True
1.0 == 1.0 
# This does not:
0.1 + 0.2 == 0.3 # False

'''
Take a look at the accumulation of error obtained during arthmetic calculations.

First, use a for loop to sum up 0.1 ten times (i.e. loop has 10 iterations).
At each iteration print:
    - The result of the total sum at each iteration to 20 decimal places.
    - The equality check between variable total and the equivalent L[ii] float
      i.e. corresponding float at position given by index ii (this is the 
      same decimal without arithmetic operation).
'''
total = 0
c     = 0.1
for ii in range(10):
    total = total + c # equivalent total += c
    print("%.20f" % total)
    print(L[ii] == total)

'''
Perform equality check of total to 1.0. Is the result True or False. 
'''    
print(total) # 0.9999999999999999
print(total == 1.0) # False!

# i.e. the following summations were the problem:
0.2 + 0.1 == 0.3 # False
0.7 + 0.1 == 0.8 # False
# And following that we had an accumulation of error.
0.8 + 0.1 == 0.9
0.9 + 0.1 == 1.0


#%% Q7 - NESTED FOR LOOPS. Only complete when finished the main questions.
# --- a)
'''
On Slide 16 you saw how 2 nested loops can be used to fill a numpy array with 
values by iterating over rows and columns of the array. Modify the code
   (1)	Write a print statement between the two for loops which will print out 
        current value of ii.
   (2)	Remove the previous print statement. Write a new print statement inside 
        the 2nd for loop which will print out current values of ii and jj.
        This should give you more understanding as to what the value of indices 
        ii and jj are at each iteration. Note: for each ii we execute all jj.
   (3)	Adjust code to fill in a 3 by 3 array with squares of numbers 1 to 9.
'''
import numpy as np
count = 1
a = np.zeros([3,5])
for ii in range(3):
    # print(ii)
    for jj in range(5):
        print(ii,jj)
        a[ii, jj] = count
        count = count + 1
print(a)      

count = 1
a = np.zeros([3,3])
for ii in range(3):
    for jj in range(3):
        a[ii, jj] = count**2
        count = count + 1
print(a)


# --- b) 
'''
Write 2 nested for loops that each iterate over a sequence generated by range(3). 
   (1)  Print out values of ii (outer loop indexing variable) and jj (inner 
        loop indexing variable) in the body of the inner most loop at each 
        iteration.
   (2)  Now re-design the loops such that printed values of jj never exceed ii. 
'''
n = 3
for ii in range(n):
    for jj in range(n):
        print(ii,jj)

n = 3
for ii in range(n):
    for jj in range(n):
        if(jj > ii):
            break
        print(ii,jj)

# --- c) EXTRA
'''
Use 2 nested loops to print the following numbers 1 - 9:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''    
for ii in range(1, 10):     # [1,2,3,4,5,6,7,8,9]
    accumStr = str(ii)
    for jj in range(ii-1):  # note: list(range(0)) returns empty result []
        accumStr += str(ii) # typecast int to str; add strings using + operator
    print(accumStr)   

# --- d)EXTRA
'''
You have the following code, state what you exptect to be printed?
Afterwards actually run the code and observe output (if any). 
'''
for ii in []:
    print(ii)
# Since the sequence (in this case empty list) does not have any eleemnts, the
# for loop has nothing to iterate over and it is therefore skipped.


