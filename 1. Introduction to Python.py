# -----------------------------------------------------------------------------
#%% Q1 Operators – Arithmetic
#%% --- 1a)
'''
Initialise x to 15. Use x inside an equation to obtain y where: y = 53 + x÷2.5
'''
x = 15; y = 5 ** 3 + x / 2.5 # note we can separate 2 lines with ; on 1 line

#%% --- 1b)
'''
i) Test if y is a positive number (store result into variable called yPositive) 
Hint: result is a True or False answer

ii) Next, test if y is even or odd (store result into variable called yEven)
Hint1: result is a True or False answer
Hint2: think about using remainder operator
'''
yPositive = y > 0  # True
yEven = y % 2 == 0 # False

#%% --- 1c)
'''
Next investigate the difference between division and floor division:
i)	Divide 67 by 6. 
ii)	Divide 71 by 6.
iii)	Now use floor division to divide 67 by 6. 
iv)	Next use floor division to divide 71 by 6.
How is the result rounded down (i.e. if division result is 11.1 or 11.8, 
                                what does floor division round it to)? 
'''
a = 67 / 6  # 11.166666666666666
b = 71 / 6  # 11.833333333333334

c = 67 // 6 # 11
d = 71 // 6 # 11

# In floor division: numbers are first divided then rounded down, 
# irrespective of decimal being 11.1 or 11.8. 

#%% --- 1d)
'''
On one line of code find (5+9) squared, then floor divided by 2, then find the 
remainder of the result with 3. Assign result to a variable, for example, x1.

Next write out the operation again, but this time explicitly place brackets 
around operations as they are executed based on operator precedence. Assign 
result to a variable, for example, x2. Check that x1 and x2 indeed agree.
'''
x1 = (5 + 9) ** 2 // 2 % 3  
x2 = (((5 + 9) ** 2) // 2) % 3  

x1 == x2    # True

#%% --- 1e)
'''
You have a variable: x3 = 17. Use shorthand notation to find a floor division 
of x3 with 3 which will overwrite variable x3 to the new value.
'''
x3 = 17
x3 //= 3    # previous value of x3 is overwritten with the new value 5

#%% --- 1f)
'''
Explain the difference between operator precedence and operator associativity.

Prove to yourself that using exponent operator on the same line, e.g. 2**2**4 
gives a different result to parenthesized version (2**2)**4 and understand why.
'''

'''
Operator Precedence – pre-determined order in which several operations 
   occurring in an expression are evaluated and resolved in the absence of 
   parenthesis. 
Operator Associativity – order in which an expression containing multiple 
   operators of the same precedence is evaluated. Typically left-to-right 
   associativity. 
'''

x4 = 2 ** 2 ** 4   # right-to-left associativity
x5 = (2 ** 2) ** 4 # default operator associativity is overwritten with ()


# -----------------------------------------------------------------------------
#%% Q2 Operators – Relational
#%% --- 2a)
'''
String "abc" equals to "abcd", where string mean anything included in ""
'''
s1 = "abc"
s2 = "abcd"
strEq = s1 == s2  # False (point-wise comparison of characters fails)

#%% --- 2b)
'''
17.5 not equal to 17.50 (note we want to check that decimal zero is not 
                         affecting the equality test result). 

Next check 5 (this will default to integer type in Python) equality to 5.0 
(this is a float type in Python).
'''
x4 = 17.5; x5 = 17.50
x4 == x5 # True (above are equivalent)

x6 = 5; x7 = 5.0
x6 == x7 # True

#%% --- 2c)
'''
Execute: 5 < 7 < 9. How could this line of code also be written? In order to 
answer this question read the explanation on the slide for relational operators
'''

5 < 7 < 9
(5 < 7) and (7 < 9) # this is what actually happens behind the scenes
'''
The expression actually is interpreted as: 5 < 7 and 7 < 9 by Python, without 
the need to chain it explicitly (unlike in R). 
Thus first 5 < 7 is compared (i.e. left-to-right associativity) if result 
obtained is True (which it is), then next 7 < 9 is compared, the result of 
which is also True, next overall expression: True and True is compared, 
result is True. 

Why in this order? Because of operator precedence, see Slide 14: the relational 
operator <  has priority of being executed first over the and operator.
'''

#%% --- 2d)
# myVar = (5>=0) or (“doggod” == “doggod”) 
'''
Copy paste this command from the pdf into a Script: 
myVar = (5 >= 0) or (“doggod” == “doggod”)
i) Check result of each parenthesised expression (to run sub-parts of a long 
expression highlight the part of interest with your mouse and press F9 “run 
selection”). 

Hint: you will see your first syntax error that can occur when pasting code 
copied from documents/online sources. The ‘why doesn’t this work - everything 
is correct?’ bug. The “ “ quotation marks character in a pdf is not the same 
character " " which is what is used for a string by UTF-8 encoder. This means 
that Python Interpreter will produce an error. Replace each pasted quotation 
mark by deleting it and typing it out again. You should see that your string 
now gets correctly recognised because it becomes green.                                                  
                                                                                                   
ii) Evaluate the whole line. Did we need to parenthesise each operand?                                              
'''

'''
The copied line won't run as the provided quotation marks of pdf are not 
recognised in Python. Need to delete and re-type them.

Note: the hat points to the place in code causing the error (quotation mark)

Note: You can spot that the quotation marks were not doing their job in the 
first instance of paste, since the strings did not get highlighted in green 
(unlike in the correct version).

Note: Technically, we do not need brackets around each operand, since or is 
below > and == in the precedence table (see Slide 14). Therefore 5 > 0 is 
compared first, next “doggod”==”doggod” is compared and then True or True is 
evaluated to give answer True.
'''

myVar = (5 >= 0) or ("doggod" == "doggod")


# -----------------------------------------------------------------------------
#%% Q3
#%% --- 3a)
'''
Perform an exhaustive check (i.e. check all combinations) on how operator 
and works. i.e. check the results of expressions: 
'''
True and True   # True 
True and False
False and False

#%% --- 3b)
'''
Do the same for or logical operator.
'''
True or True    # True 
True or False   # True 
False or False  # False

#%% --- 3c)
'''
Check output of not operator for the following expressions: 
'''
not True
not False
# Remember not operator reverses the logic

#%% --- 3d)
'''
Let’s combine operators on the same line:
i.	Examine and explain the execution order of operators in below's expression: 
'''
17 != 5 or 12 == 12 and 15 < 1 
# All relational operators are evaluated first, then and, then or

17 != 5 or (12 == 12 and 15 < 1) 
# parenthasized but does the same as above. Equivalent to True or False
'''
ii.	Next analyse the below parenthesised version and understand why the result  
is different to the version without parenthesis above: 
'''
(17 != 5 or 12 == 12) and (15 < 1)
# parenthesis overwrite default operator precedence, to provide you the 
# intended result

#%% --- 3e) EXTRA 
'''
Examine outputs of the following lazy evaluations:
'''
True and True and True # True
1 and True and True    # True
1 and 1 and True       # True
1 and 1 and 1          # True
# Remember that Python will return the value of the last evaluated argument

False and True and True # Returns False
0 and True and True     # 0 and True is false. Python returns 0 'lazily'

# 0 and True and anyAlphaNumeric 
'''
0 and True is false, hence right side is never evaluated; 
Python is acting 'lazily'. 
'''


# -----------------------------------------------------------------------------
#%% Q4
# --- 4a) 
'''
Practice 3 best ways of importing the math module and using the sqrt() 
function to find sqrt of 25, store result to a varaible called 'x'.

After you finish practicing each import command, delete the current objects
from the session using %reset magic command in the Console. This will ensure
that your previous import command is erased and you are starting fresh. 
'''
# Way 1:
# import PACKAGE -> load a whole package (good practice)
import math                # load math package
x1 = math.sqrt(25)         # find sqrt
# Run %reset in the Console

# Way 2:
# import PACKAGE as SHORTHANDNAME -> load a whole package (good practice)
import math as mt          # load math module and give it a shortered name
x2 = mt.sqrt(25)           # find sqrt
# Run %reset in the Console

# Way 3:
# from PACKAGE import NAME -> statement specific import (good practice)
from math import sqrt    # load a particular function from math package
x3 = sqrt(25)      # find sqrt 
# Run %reset in the Console

# NOTE: when you need to use a library, it is best to make all of the import
# commands at the top of the file, this is good coding practice.

#%% --- 4b) 
'''
Given your knowledge of math and the mathematical operators, what is another 
quick way of finding the sqrt of 25 without using a library?
'''
x4 = 25 ** 0.5 

#%% --- 4c) 
'''    
Import both sqrt and pi from the math library. Print the value pi.
'''
from math import sqrt, pi
print(pi)

#%% --- 4d) 
'''
Import the numpy library and list all of the available resources 
(i.e. variables and functions available in the library).
'''
import numpy
dir(numpy)

#%% --- 4e) 
'''  
Next you will practice how to import contents of another file into your Script.
You have an lmdict.py file, which contains a dictionary with positive and 
negative words, to be used in sentiment analysis. 

Import the 'lmdict.py' module into your current Script, using command
import library

List all of the resources (you will see functions with _ _ NAME _ _ these are
meant to be called internally, ignore them). You will also see the varaible 
contained in that file: lmdict (as it happens, variable has the same name as 
                                the file, which is ok).

Store the variable lmdict to a new variable in your Script, call your variable 
sentimentDictionary. 

Hover over the sentimentDictionary variable in your Variable Explorer & double
click on it. The variable will open up. You will see it is a dictionary with 2
elements, each element contains a list of words.

It is now ready for use.
'''

# Load lmdict's contents:
import lmdict

dir(lmdict)

sentimentDictionary = lmdict.lmdict

# Run %reset in the Console

#%% --- 4f)
'''
What is the quicker way of importing the variable lmdict from the file lmdict?
'''
from lmdict import lmdict

# -----------------------------------------------------------------------------
#%% Q5
# a) --------------------------------------------------------------------------
'''
Calculate the SR based on hypothetical values given below. Assign a suitably 
named variable that stores the result of your SR calculation. You must use only 
one line of code and you are not allowed to use the math.sqrt() command to 
calculate square roots. [Please come up with an alternative for the square 
root calculation; HINT: think about the arithmetic operators and how these can 
help you]. 

Portfolio average return 0.1, variance of returns 0.0625, risk-free rate 0.02.
'''

SR = (0.1 - 0.02) / (0.0625 ** 0.5) # 0.32

# b) --------------------------------------------------------------------------
'''
Financial comprehension question: Why can we not simply use the annual return 
by itself to measure a strategy’s performance? (Hint: consider the need to 
compare SR across different strategies in order to select the best one).
'''

'''
In order to compare effectiveness of different strategies, the ‘risk’ 
(i.e. how much does that strategy vary and is likely to be volatile) has to be 
taken into account. For strategies with the same SR but different volatilities, 
the one with lowest vol. would be selected. 

Note: Sharpe Ratio penalises upside and downside volatility equally. Other 
measures exist which only penalise the downside aspect of vol, these are 
a) Sortino Ratio 
b) Differential Sharpe Ratio.
'''


#%% Q6
# a) --------------------------------------------------------------------------
# --- 6a) 
'''
Make a comment on:
    Can an object's identity, type, value be changed? 
'''
# Identity: NO
# Type    : NO (but can be typecast, so only under certain conditions)
# Value   : YES if object is mutable, NO for immutable objects

#%% --- 6b)
'''
You have an object baseRateBOE = 0.75. 
Establish what is this object’s identity, type and value.
'''
baseRateBOE = 4.25
# identity
id(baseRateBOE)
type(baseRateBOE)
print(baseRateBOE)

#%% --- 6c) [Identity practice] 
'''
You have another object baseRateFED = 0.50. 
Establish if these two objects (baseRateBOE and baseRateFED) point to the same 
location in memory.
'''
baseRateFED = 5.00
baseRateBOE is baseRateFED
# Answer is False, ie they are different objects

#%% --- 6d) [Value practice] 
'''
Perform an equality check to establish if base rate in UK equals that of USA. 
Assign the result to a variable with identifier ratesAreEqual. 
'''
ratesAreEqual = baseRateBOE == baseRateFED
# False, the values contained inside these two objects are indeed different


#%% --- 6e) 
'''
Create two lists L1 and L2, such that:
    (version a) alias between two lists is formed.
    (version b) no alias is present.

In each case prove that it was done as requested. 
'''
L1 = [1,2,3]
L2 = L1 # alias created
print(L1 is L2) # True (both reference the same object)

L1 = [1,2,3]
L2 = list(L1) # typecasting L1 to a list breaks alias
L2 is L1 # False

# --- 6f) [EXTRA] Aliasing (Lists)
'''
You are given two lists L1 and L2.
Examine whether the two variables point to the same object?

The fact that L2 contains a reference to L1 inside of it is important!
Examine whether the L1 and 2nd element of L2, you can access it with L2[1], 
point to the same object?

Mutate the first element in L1, using L1[0] = 10
Print contents of L1 and L2. This is an example of aliasing.
'''
L1 = [1,2,3]
L2 = ["abc", L1]   # List with 2 elements: 'abc' and [1, 2, 3]
print(L1 is L2)    # False (variables point to different objects) 
# BUT!!! L2 contains a refernce to L1
print(L1 is L2[1]) # True!!! i.e. L1 and element 2 of L2 are the same object
# Mutate an element in L1
L1[0] = 10
print(L1)          # [10, 2, 3]
print(L2)          # ['abc', [10, 2, 3]]
