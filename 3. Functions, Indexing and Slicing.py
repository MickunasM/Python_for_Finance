import numpy as np

#%% Q1. FUNCTIONS USER-DEFINED -----------------------------------------------:
#  --- a) ABSOLUTE VALUE FUNCTION FOR A NUMERIC
'''
Create a fn which finds an absolute value of a numeric type (int/float).
'''
# Function Definition Goes Here:
def absVal(x): 
    if x < 0:
        return -x # note do not use abs() here as we are trying to wrte an abs
    # function ourselves
    else:
        return x

'''
Test the function using -10:
'''
# Function Call Goes Here:
ans = absVal(-10)
print(ans)
assert(ans > 0) # if this fails, code will stop executing


# --- b) MINIMUM NUMBER 
'''
Create a function which finds a minimum from 2 numeric types (int/float). 
'''
# Function Definition Goes Here:
def minNum(x, y):
    if x <= y:
        return x
    else:
        return y

'''
Test the function on numbers 2 and 5:
'''
# Function Call Goes Here:
ans  = minNum(2, 5)
print(ans) # 2


# --- c) MAXIMUM NUMBER 
'''
This is the maxNum() function you've seen in the slides:
'''
# Function Definition Goes Here:
def maxNum(x, y):
    if x >= y:
        return x
    else:
        return y
    
'''
Create an alternative way of writing the minNum function, which only involves 
a single function call to maxNum function.

Hint1: you can call any function you created from inside another function so 
       long as it has already been defined in the code above it.

Hint2: Think of passing in negative inputs to the maxNum function. Try out to 
       see what you get for maxNum(-2, -5).

'''

# Alternative minNum which calls maxNum from inside!
def minNum2(x, y):
    return -maxNum(-x, -y)
ans2 = minNum2(2, 5)

'''
Test the function on numbers 2 and 5:
'''
# Function Call Goes Here:
ans = maxNum(2.3, 5.5)
print(ans) # 5.5
ans2 = maxNum(-2, -5)
print(ans2) # -2

   
# --- d) MINIMUM NUMBER FROM A LIST OF NUMERICS
'''
Create a fn to find a min number from a list of numeric types (int/float). 
'''
# Function Definition Goes Here:
def minList(L):
    minVal = L[0]
    for ii in L[1: ]:
        minVal = minNum(minVal, ii) # calculate current min value and store it
    return minVal

'''
Test the function on: 
'''
# Function Call Goes Here:
L = [1, 2, 3, 4, 5]
ans = minList(L)
print(ans) # 1

# --- e) MAXIMUM NUMBER FROM A LIST OF NUMERICS
'''
Create a fn to find a max number from a list of numeric types (int/float). 
'''
# Function Definition Goes Here:
def maxList(L):
    maxVal = L[0] # current max value
    for ii in L[1:]: # compare to each element of list from 1 to end
        ## OPTION 1
#        if ii > maxval:
#            maxval = ii
        ## OPTION 2
        maxVal = maxNum(maxVal, ii)
    return maxVal

'''
Test the function on: 
'''
# Function Call Goes Here:
L = [1, 2, 3, 4, 5]
ans = maxList(L)
print(ans) # 5



#%% Q2 Creating Numpy Arrays
# --- a) i.e. we are using lists to convert them to np arrays
'''
Use np.array() (which accepts sequence-like objects including other arrays and 
                produces a new numpy array) to create arrays from: 
-	List [1, 2, 3]
-	List [1.0, 2, 3.] (remember the trailing zero is not necessary when 
                       specifying floats, just the dot is enough).
-	List of lists [[1,2,3], [4,5,6]]
'''
a1 = np.array([1,2,3])      # array([1, 2, 3])   all ints
a2 = np.array([1.0, 2, 3.]) # array([1., 2., 3.]) converts ints to floats
a3 = np.array([[1,2,3], [4,5,6]]) 
# size is inferred to 2D since list contains 2 elements
# array([[1, 2, 3],
#        [4, 5, 6]])

# --- b)
'''
Use the commands:
    shape : to establish the size of each dimension 
    dtype : to establish the data type of the last 2 arrays you created
'''

s2 = a2.shape   # (3,)    i.e. 1D vector of length 3
s3 = a3.shape   # (2, 3) i.e. a 2D vector of size 2 rows, 3 columns

print(a2.dtype) # float64 (meaning standard double precision floating point 
# value taking 8 bytes of 64 bits. Compatible with C double and Python float).
print(a3.dtype) # int64

# --- c) all float types, but return uninitialised garbage vals, occationally 0.0
'''
Use np.empty() to create a 1D, 2D and 3D array with the size of your choice. 
Re-run the code several times to see if the created arrays contain different 
values than the ones you observed the first time. 

Conclusion? Is it safe to assume that np.empty() will return an array of 0s?
'''
a4 = np.empty([3])
print(a4)

a5 = np.empty([3,4])
print(a5)
a6 = np.empty([2,3,4])
print(a6)

# --- d)
'''
Create two 3x4 2D arrays: one filled with 0s and another filled with 1s.
'''
a7 = np.zeros([3,4])
print(a7)
"""
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
"""
a8 = np.ones([3,4])
"""
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
"""

# --- e) 
'''
Introducing np.asarray(). You have 3 arrays created below via different methods     
-	Check whether there is an alias between a-b and a-c 
    (i.e. whether two variables point to the same location in memory).
-	Change the value of array a in position 1 (indexed by 0) to 11. 
    Check contents of array a, b, c.
'''
a = np.array([1,2,3]) 
b = np.array(a)   # i.e. b is a copy of a (new object) 
c = np.asarray(a) # i.e. c is a view of a (same object)

a is b # False
a is c # True (i.e. a and c point to the same location in memory)

# Note the asarray method does not copy the data if it is already an array, 
# thus creating an alias. Any mutation performed on array 'a' will be relected 
# in array 'c', but not in array b.    

a[0] = 11
print(a, b, c) # c is mutated when a is changed, but not b.

'''
Explanation: the np.asarray() performs the same job as np.array() however 
does not copy input if it is already an ndarray of the same datatype.
'''

#%% Q3 Arithmetic operations, Mathematical / Statistical calculations
# --- a)
'''
Create a 1-D array of prices for Intel, call it intc containing values 55, 42, 61. 
-	Establish max value contained in intc
-	Establish the index at which max value occurs in intc
'''
intc = np.array([55, 42, 61])

intc_max = np.max(intc)
ind = np.argmax(intc) # index is 2, since max element is in 3rd position


# --- b)
'''
Create an array called a using a list of lists: [[1., 2., 3.], [4., 5., 6.]]. 
Your task is to perform the following element-wise operations:
-	Multiply a by a
-	Take a away from a
-	Find reciprocal of a
-	Find square root of a
'''
a = np.array([[1., 2., 3.], [4., 5., 6.]])

a1 = a*a
# array([[ 1.,  4.,  9.],
#        [16., 25., 36.]])

a2 = a-a
# array([[0., 0., 0.],
#        [0., 0., 0.]])

a3 = 1/a
# array([[1.  , 0.5, 0.33333333],
#        [0.25, 0.2, 0.16666667]])

a4 = a**0.5 
# array([[1., 1.41421356, 1.73205081],
#        [2., 2.23606798, 2.44948974]])

a_max = np.max(a)

a_argmax = np.argmax(a)


# --- c)
'''
You have the following 1-D array: a = np.arange(9)
First, re-shape this array into a 2-D 3-by-3 array using numpy.reshape() method 
(if unsure read official documentation here 
 https://numpy.org/doc/stable/reference/generated/numpy.arange.html
 get familiar with how official documentation looks). 

Find sum, mean, std (with and without ddof=1 optional argument) and cumsum for:
-	Whole array
-	Dimension axis = 0
-	Dimension axis = 1

Note:  name your variables in a descriptive way, for example for sum use: 
       a_sum, a0_sum, a1_sum etc

Note2: remember that np.std() function calculates standard deviation either 
       using 1/N or 1/(N-ddof) specified by the optional arguement to the fn.
'''
b = np.array([[0.1,2.1,32], [0.9,15,5.6]])
a5 = a > b
# array([[ True, False, False],
#        [ True, False,  True]])

a = np.arange(9).reshape(3,3)
"""
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
"""
a_sum  = a.sum()         # 36
a0_sum = a.sum(axis=0)   # array([ 9, 12, 15])
a1_sum = a.sum(axis=1)   # array([ 3, 12, 21])

a_mean  = a.mean()       # 4
a0_mean = a.mean(axis=0) # array([3., 4., 5.])
a1_mean = a.mean(axis=1) # array([1., 4., 7.])

a_std    = a.std()               # 2.581988897471611
a_std_2  = a.std(ddof=1)         # 2.7386127875258306
a0_std   = a.std(axis=0)         # array([2.44948974, 2.44948974, 2.44948974])
a0_std_2 = a.std(axis=0, ddof=1) # array([3., 3., 3.])
a1_std   = a.std(axis=1)         # array([0.81649658, 0.81649658, 0.81649658])
a1_std_2 = a.std(axis=1, ddof=1) # array([1., 1., 1.])

a_cumsum  = a.cumsum()   # array([ 0,  1,  3,  6, 10, 15, 21, 28, 36])
a0_cumsum = a.cumsum(axis=0)  # DOWN ROWS
# array([[ 0,  1,  2],
#        [ 3,  5,  7],
#        [ 9, 12, 15]])
a1_cumsum = a.cumsum(axis=1) # ACROSS COLUMNS
# array([[ 0,  1,  3],
#        [ 3,  7, 12],
#        [ 6, 13, 21]])

# EXTRA
# --- d) element-wise vectorised comparisons resulting in boolean variable type
'''
You have an array names, given below.
-	Use relational operator == to obtain a boolean array boolBob which gives 
    True or False answer of where array names contains name ‘Bob’ and another 
    boolean array boolWill for ‘Will’.
-	Reverse the logic of the array boolBob
-	Create a new boolean array which is a result of a check for either boolBob 
    or boolWill. 
'''
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) # 7x1
boolBob  = names == 'Bob'        
#      array([ True, False, False,  True, False, False, False])

boolWill = names == "Will"       
#      array([False, False,  True, False,  True, False, False]) 

boolNotBob  = ~ boolBob          
# not: array([False,  True,  True, False,  True,  True,  True])

bob_or_will = boolBob | boolWill 
# or:  array([ True, False,  True,  True,  True, False, False])


#%% Q4
# --- 4a) SLICING CREATES A VIEW ON THE ARRAY
'''
Create array of numbers from 0 to 9 using array’s range function, and call it a
-	Use an index to extract element in position 5
-	Extract the following slice: [5,6,7] and assign it to a variable called 
    a_slice
-	Overwrite elements of a_slice with a_slice[:] = 12 using the 
    ‘bare’ slice [:] which will assign all values in the array to 12. 
    Here we ‘broadcast’ i.e. propagate the value to the entire section. 
    Observe what original array has been changed to.

The reason Python does not create copies of original array is because NumPy was 
designed to work on large arrays. The performance and memory problems are thus 
avoided by providing views.
If you require to explicitly copy a part of an array use the following command: 
a[5:8].copy()
'''
a = np.arange(10)
a[5]   # 5

a_slice = a[5:8] # 
print(a_slice)   # array([5, 6, 7])

a_slice[:] = 12  # broadcasting (i.e. value propagated across entire section)
print(a_slice)   # array([12, 12, 12])

print(a) # [ 0  1  2  3  4 12 12 12  8] note mutation is reflected in original 
# array since this was a view not a copy.


# --- 4b)
'''
Your have an array given below:
'''
a = np.zeros(36).reshape(6,6)
a[0,] = list(range(6))
a[1,] = list(range(10,16))
a[2,] = list(range(20,26))
a[3,] = list(range(30,36))
a[4,] = list(range(40,46))
a[5,] = list(range(50,56))

'''
Practice using indexing and slicing by running commands below. Ensure to 
understand how the command extracts data from the array.
'''
# execute single line at a time and observe the output
print(a)
a[0]        # array([0., 1., 2., 3., 4., 5.])
a[0, 3:5]   # array([3., 4.])
a[4:, 4:]   # array([[44., 45.],
#                    [54., 55.]])
a[:, 2]     # array([ 2., 12., 22., 32., 42., 52.])
a[2::2, ::2]  # array([[20., 22., 24.],
#                      [40., 42., 44.]])

# --- 4c)
'''
Recap:
-	In a 2D array what axis do rows go by 0 or 1?
-	If you slice an array do you get a copy or a view on the original array? 
    And what does that mean?
'''
# row is axis 0
# column is axis 1

# Slicing gives a view. It means that all mutations done on the slice will be 
# seen in the original array.



#%% Q5
# --- 5a) 
'''
You have an array of returns given below.
-	Sort the array in ascending order first using Rt.sort()
-	Print out contents of Rt. Did you expect contents to change or did you 
    expect Rt array to remain unchanged?).
-	Depending on the task, you may wish to keep a copy of your original data 
    unchanged and create a new ordered returns data. Start afresh by 
    re-initialising variable Rt. Then, what command would you need below to 
    obtain a copy of Rt after sorting it:
    Rt_sorted = ?
    Hint: use top-level numpy sort function
-	Check original array Rt to ensure it was not affected by your above sort. 
    Also print out the contents of Rt_sorted which should have your sorted data
'''
Rt = np.array([ 0.0471435, -0.0190975,  0.0432706, -0.031265, -0.0720588]) 
Rt.sort() # no output as it sorts array directly (i.e. operating 'in place')
print(Rt) # [-0.0720588 -0.031265  -0.0190975  0.0432706  0.0471435]
# original array Rt sorted

Rt = np.array([ 0.0471435, -0.0190975,  0.0432706, -0.031265, -0.0720588]) 
Rt_sorted = np.sort(Rt) # creates an output that needs to be assigned to new 
#                         variable (i.e. result is copied)
print(Rt) # [0.0471435 -0.0190975 0.0432706 -0.031265  -0.0720588] 
# Rt not affected
print(Rt_sorted) # [-0.0720588 -0.031265  -0.0190975  0.0432706  0.0471435]


# --- 5b)
'''
You have two arrays: 
    (2,) vector of 1s and a 
    (2,2) var-cov matrix, which looks like this
              Growth    Value
       Growth 0.002824  0.003178
       Value  0.003178  0.002824
-	Re-create the numpy arrays (omitting row/column labelling for now).
-	Find inverse of the vcov_r, call it vc_inv
-	Check the shape of ones and vc_inv varaibles and review if dot product is 
    acceptable. 
-	Find a dot product between a vector of ones and the inverse you just found  
    above. 
''' 
ones = np.ones(2)
vcov_r = np.array([[0.002824, 0.003178], [0.003178, 0.002824]])

vc_inv = np.linalg.inv(vcov_r) 
print(vc_inv)

ones.shape # (2,)
vc_inv.shape # (2,2)
# Yes dot product is appropriate since we have a vector and a matrix where 
# last axis dimensions agree. Therefore we carry out a (2,) times (2,2). In
# linear algebra terms this is equivalent to 2x2 times 2x1 resulting in 2x1 vec

ans = np.dot(ones, vc_inv)
print(ans)

# --- 5c) [EXTRA]
'''
To create a matrix containing 1s on the diagonal and 0s on the off diagonal, 
called I in maths (stands for ‘Identity’), we can use np.eye(n) or equivalently 
np.identity(n). 
-	Create a matrix containing the following five diagonal entries: 
    0.1, 0.2, 3, 2, 5.5.
'''
temp = np.eye(5) # np.identity(5)
a9 = temp * [0.1, 0.2, 3, 2, 5.5]
"""
array([[0.1, 0. , 0. , 0. , 0. ],
       [0. , 0.2, 0. , 0. , 0. ],
       [0. , 0. , 3. , 0. , 0. ],
       [0. , 0. , 0. , 2. , 0. ],
       [0. , 0. , 0. , 0. , 5.5]])
"""


#%% NUMPY EXTRA
# 5d) --- BOOLEAN INDEXING
'''
Boolean Indexing – you are allowed to index array with boolean arrays. 
The boolean array has to be the same length as the array’s axis it is indexing. 

numpy.random module generates arrays of sample values from many kinds of 
probability distributions:
    rand    – uniform distribution
    randint – integers from a given low-high range
    randn   – standard normal distribution (mean=0, std=1)

-	Use the randn function to create a 7x4 array of random numbers, called r.
    The seeding will allow reproducibility of results.
'''

# fixing random number generator so that results can be reproduced
np.random.seed(1234) 
r = np.random.randn(7,4)
"""
array([[ 4.71435164e-01, -1.19097569e+00,  1.43270697e+00,  -3.12651896e-01],
       [-7.20588733e-01,  8.87162940e-01,  8.59588414e-01,  -6.36523504e-01],
       [ 1.56963721e-02, -2.24268495e+00,  1.15003572e+00,   9.91946022e-01],
       [ 9.53324128e-01, -2.02125482e+00, -3.34077366e-01,   2.11836468e-03],
       [ 4.05453412e-01,  2.89091941e-01,  1.32115819e+00,  -1.54690555e+00],
       [-2.02646325e-01, -6.55969344e-01,  1.93421376e-01,   5.53438911e-01],
       [ 1.31815155e+00, -4.69305285e-01,  6.75554085e-01,  -1.81702723e+00]])
"""

'''
Here we create a boolBob array which indicates positions of name ‘Bob’ in names 
'''
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) # 7x1
boolBob = names == 'Bob'  
bobRows = r[boolBob]
""" 2x4 array
array([[ 0.47143516, -1.19097569,  1.43270697, -0.3126519 ],
       [ 0.95332413, -2.02125482, -0.33407737,  0.00211836]])
"""

'''
-	Now extract only those rows which do not correspond to ‘Bob’. 
    (Hint: use the array not operator to reverse the boolBob logic).
'''

notBobRows = r[~ boolBob]
"""
array([[-0.72058873,  0.88716294,  0.85958841, -0.6365235 ],
       [ 0.01569637, -2.24268495,  1.15003572,  0.99194602],
       [ 0.40545341,  0.28909194,  1.32115819, -1.54690555],
       [-0.20264632, -0.65596934,  0.19342138,  0.55343891],
       [ 1.31815155, -0.46930528,  0.67555409, -1.81702723]])
"""      

'''
-	Extract rows of random array which correspond to either boolBob or boolWill.
'''
boolWill    = names == "Will"
bob_or_will = boolBob | boolWill
bob_or_will_rows = r[bob_or_will, :] # or can omit the second dim as above
"""
array([[ 4.71435164e-01, -1.19097569e+00,  1.43270697e+00,  -3.12651896e-01],
       [ 1.56963721e-02, -2.24268495e+00,  1.15003572e+00,   9.91946022e-01],
       [ 9.53324128e-01, -2.02125482e+00, -3.34077366e-01,   2.11836468e-03],
       [ 4.05453412e-01,  2.89091941e-01,  1.32115819e+00,  -1.54690555e+00]])
"""


# 5e) --- FANCY INDEXING
'''
Fancy Indexing – term used for indexing arrays using integer arrays.
All of the usual slicing rules apply to arrays also, for example negative 
indexing would select rows from the end. 
Perform the following operations on array a provided below and analyse output:
-	a[[4,3,0,6]]
-	a[[-3,-5,-7]]
Unlike slicing, fancy indexing always copies the data.
'''
a = np.empty([8,4])
for ii in range(8):
    a[ii] = ii

copy1 = a[[4,3,0,6]]
"""
array([[4., 4., 4., 4.],
       [3., 3., 3., 3.],
       [0., 0., 0., 0.],
       [6., 6., 6., 6.]])
"""
copy2 =	a[[-3,-5,-7]]
"""
array([[5., 5., 5., 5.],
       [3., 3., 3., 3.],
       [1., 1., 1., 1.]])
"""


# 5f) TIMING FOR LOOPS VS NUMPY ARRAYS
'''
Numpy’s library of algorithms are written in C. This means that numpy arrays 
require much less memory than built-in Python sequences. Equally the ability of 
operations to perform computations on entire arrays without for loops makes 
them more suitable for majority of numerical data processing.

In this question we are going to investigate the speed of computation using a 
list and a numpy array. We would like to check computation time in milliseconds 
of a multiplication by 2 of each element of a list and an array, when 
performing that computation 10 times. Initial variables are:
-	List of 1,000,000 numbers e.g. 0-999999
-	Numpy array of same 1,000,000 numbers
Use 2 different ways of timing executions, described in way i) and ii) below.
'''
# TWO WAYS OF CHECKING TIME. WAY 1 INSIDE SCRIPT

'''
The time of executions can be measured using code written in the script (here).
'''
import time

L = list(range(1000000))
a = np.arange(1000000)

# perform list timing
start = time.time()
for _ in range(10):
    newL  = [2*x for x in L]
end   = time.time()
t_L   = end-start
print("List time: ", t_L*1000, 'ms') # time in seconds

# perform numpy array timing
start2 = time.time()
for _ in range(10):
    newa  = 2*a
end2 = time.time()
t_a  = end2-start2
print("Array time: ", t_a*1000, 'ms') # time in seconds

'''
The time of executions can be measured using %time magic command in the Console

Note you are allowed to write a one line for loop on a single line. 
For example if you had:
for ii in range(10):
    x = print(ii)
you could execute this in Console as:
for ii in range(10): x = print(ii)

Execute the following in the console:
'''
# WAY TWO: IN CONSOLE:
# %time for _ in range(10): newL = [2*x for x in L]
# %time for _ in range(10): a2 = 2*a
