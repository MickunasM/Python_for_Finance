from urllib.request import urlopen # import function urlopen
from bs4 import BeautifulSoup      # import function BeautifulSoup

import nltk # natural language processing library (nat. lang. toolkit)
from nltk.sentiment.vader import SentimentIntensityAnalyzer # sentiment anal

import webbrowser
import certifi
import ssl
import requests

#%% Q1 SCRAPE FED STATEMENT HTML FILE ----------------------------------------:

#html = urlopen('https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm',context=ssl.create_default_context(cafile=certifi.where()))
#html = urlopen('https://pythonscraping.com/pages/page1.html', context=ssl.create_default_context(cafile=certifi.where()))
    

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
url = 'https://www.federalreserve.gov/newsevents/pressreleases/monetary20200315a.htm'
r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.content, "html5lib")  
print(bs) # you will see the entire read in HTML page starting from <html> and
          # ending with </html> 

# --- SUBOPTIMAL SOLUTIONS
# Next we try to find which solution we should use to get only Statement text:
# Sub-optimal solution1 :
data = bs.find_all('p') # extracts all paragraphs not just the Statement text
print(data) # scroll up to see useless <p> tags that were also pulled down

# Sub-optimal solution2 :
data = bs.find('div', {'id':'content'})
print(data) # also reads too many paragraphs <p> which are not the Statement

# Sub-optimal solution3 :
data = bs.find('div', {'id':'article'})
print(data) # getting there but still too many paragraphs <p> 

# --- OPTIMAL SOLUTION:
# situate yourself inside the actual start of paragraphs given by tag:
# <div class="col-xs-12 col-sm-8 col-md-8">
# Check other statements to see this tag always being used before the Statement
x = bs.find('div', {'class':'col-xs-12 col-sm-8 col-md-8'})
type(x) # bs4.element.Tag
print(x) # We are very close but at the top and bottom you'll see <div> tag
# We can 'chain' the tags, within current html material find all tags <p>
data = x.find_all('p') # list of 10 entries (i.e. 10 paragraphs)
type(data)          # bs4.element.ResultSet
print(data)         # all 6 main pragraphs 

type(data[0])       # bs4.element.Tag
print(data[0])      # first paragraph with text in form of a tag

print(data[0].text) # first paragraph with text only

# --- CONVERT PARAGRAPH TAGS TO STRINGS ---------------------------------------
# --- Solution A:
s = ''
for ii in range(4):
    s = s + " " + data[ii].text
print(s) 
type(s) # str


# --- Solution B:
# Use your knowledege of string mehtods and the following to help with the task
# 1) data[ii].text extracts str for ii(th) paragraph 
# 2) the Statement text always ends with a paragraph starting with:
signalEnd = "Voting for the monetary policy action were"

s = '' # we will build the final string by starting with an empty str
for ii in data: 
    if signalEnd not in ii.text:
        s = s + " " + ii.text # need to add a space
    else:
        break # break out as soon as you find the signal to end

print(s) # String is ready for further use!!!
'''
The coronavirus outbreak has harmed communities and disrupted economic activity 
in many countries, including the United States.
...
The Committee will continue to closely monitor market conditions and is 
prepared to adjust its plans as appropriate. 
'''


#%% Q2. DICTIONOARIES ---------------------------------------------------------:
# a) 
# 1st option 
# defaults to iterating over keys i.e. ii gets assigned a key on each iteration
months = {'Jan':1, 'Feb':2, 'Mar':3}
for ii in months:
    print(ii, months[ii])
# Jan 1
# Feb 2
# Mar 3

# 2nd option 
# explicitly accessing keys to iterate over
for ii in months.keys():
    print(ii, months[ii])
# Jan 1
# Feb 2
# Mar 3
    
# b)
instruments = dict() # alternatively instruments = {}

# c)
maturity = 0.25 
faceVal = 100
coupon = 0.0
price = 97.5
freq = 2

# d)
instruments[maturity] = (faceVal, coupon, price, freq)

# e) 
len(instruments) # 1

# f)
# type months. then press Tab

# g)
# copy of what you should have extracted form Fed website:
s = "The coronavirus outbreak has harmed communities and disrupted economic activity in many countries, including the United States. Global financial conditions have also been significantly affected. Available economic data show that the U.S. economy came into this challenging period on a strong footing. Information received since the Federal Open Market Committee met in January indicates that the labor market remained strong through February and economic activity rose at a moderate rate. Job gains have been solid, on average, in recent months, and the unemployment rate has remained low. Although household spending rose at a moderate pace, business fixed investment and exports remained weak. More recently, the energy sector has come under stress. On a 12‑month basis, overall inflation and inflation for items other than food and energy are running below 2 percent. Market-based measures of inflation compensation have declined; survey-based measures of longer-term inflation expectations are little changed. Consistent with its statutory mandate, the Committee seeks to foster maximum employment and price stability. The effects of the coronavirus will weigh on economic activity in the near term and pose risks to the economic outlook. In light of these developments, the Committee decided to lower the target range for the federal funds rate to 0 to 1/4 percent. The Committee expects to maintain this target range until it is confident that the economy has weathered recent events and is on track to achieve its maximum employment and price stability goals. This action will help support economic activity, strong labor market conditions, and inflation returning to the Committee's symmetric 2 percent objective. The Committee will continue to monitor the implications of incoming information for the economic outlook, including information related to public health, as well as global developments and muted inflation pressures, and will use its tools and act as appropriate to support the economy. In determining the timing and size of future adjustments to the stance of monetary policy, the Committee will assess realized and expected economic conditions relative to its maximum employment objective and its symmetric 2 percent inflation objective. This assessment will take into account a wide range of information, including measures of labor market conditions, indicators of inflation pressures and inflation expectations, and readings on financial and international developments. The Federal Reserve is prepared to use its full range of tools to support the flow of credit to households and businesses and thereby promote its maximum employment and price stability goals. To support the smooth functioning of markets for Treasury securities and agency mortgage-backed securities that are central to the flow of credit to households and businesses, over coming months the Committee will increase its holdings of Treasury securities by at least $500 billion and its holdings of agency mortgage-backed securities by at least $200 billion. The Committee will also reinvest all principal payments from the Federal Reserve's holdings of agency debt and agency mortgage-backed securities in agency mortgage-backed securities. In addition, the Open Market Desk has recently expanded its overnight and term repurchase agreement operations. The Committee will continue to closely monitor market conditions and is prepared to adjust its plans as appropriate. "

temp1 = s.replace(',', '').replace('.', '').replace('-',' ') # take away all , and .
temp2 = temp1.lower() # convert all upper case words to lower case
L = temp2.split(' ')  # split 1 string into words which become elems of a list
numWords = len(L)     # 523 words to be analysed

d = {}
for ii in L:       # elems of L are words as strings i.e. 'key' form
    if ii in d:    # if key already in dictionary
        d[ii] += 1 # up occurance of word (i.e. key) in sentense by 1
    else:          # if key not yet in dictionary, create it
        d[ii] = 1  # NOTE: here we create first entry for each KEY ii
numKeys = len(d)   # 232
d.items()          # alternatively print(d) will dispay the dictionary

# h) Perform Simple Sentiment Analysis on the data
from lmdict import lmdict
score = 0 # total sentiment score
counter = 0

for k in d: # looping over keys
    if k in lmdict['Positive']:
        score += d[k] # add current value total score
        counter += 1
    if k in lmdict['Negative']:
        score -= d[k] 
        counter += 1

avScore = score / counter
print('Fed Statement Sentiment Estimate', '%.2f' % avScore)
# Comment 0.33 on scale of -1 and +1 is mildly positive.


# iv) --- [EXTRA]
score = 0 # total sentiment score
counter = 0
for ii in range(len(L)): # looping over words from the final list directly
    word = L[ii]    
    # For the first 2 words:    
    if ii < 2: 
        if word in lmdict['Positive']:
            score += d[k] # add current value total score
            counter += 1
        if word in lmdict['Negative']:
            score -= d[k] 
            counter += 1
    # for word 3 onwards
    else:
        if word in lmdict['Positive']:
            if L[ii-1] in lmdict['Negate'] or L[ii-2] in lmdict['Negate']:
                score -= d[k] 
                counter += 1
            else:
                score += d[k] # add current value total score
                counter += 1
        if word in lmdict['Negative']:
            score -= d[k] 
            counter += 1

avScore = score / counter
print('Fed Statement Sentiment Estimate', '%.2f' % avScore)
# Comment 0.25 on scale of -1 and +1 is mildly positive.


# v) [EXTRA]
import nltk # natural language processing library (nat. lang. toolkit)
from nltk.sentiment.vader import SentimentIntensityAnalyzer # sentiment anal

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer() # init VADER, such that its ready for use
'''
Each word in a list is analysed for its negative / neutral / positive valence.
Then sentiment analyser produces a 'polarity score', standardized to range 
-1, +1, which gives the overall affect of the entire text.
'''

# Option 1 (working with words)
n = len(L) # number words in the list
scores = []
for ii in range(n):
    word = L[ii] # obtain word at index ii
    d = sid.polarity_scores(word) # dictionary of results
    compoundPolarity = d['compound']
    if abs(compoundPolarity) > 1e-5:
        scores.append(d['compound'])

sum(scores)/len(scores) # 0.15 on a mild positive side

# Option 2 (working with sentnces)
L = s.split('.') # split 1 string into words which become elems of a list
n = len(L)       # number sentences in the list
scores = []
for ii in range(n):
    sentence = L[ii] # obtain sentence at index ii
    d = sid.polarity_scores(sentence) # dictionary of results
    compoundPolarity = d['compound']
    if abs(compoundPolarity) > 1e-5:
        scores.append(d['compound'])

sum(scores)/len(scores) # 0.20


#%% Q3. COMPREHENSIONS -------------------------------------------------------:
# a) LIST
T = (1,2,3,4,5)
L = [ii**3 for ii in T if (ii % 2 != 0)]
print(L) # note the result is a list! [1, 27, 125]

# b) Original long way of writing out each letter from string
L = []
for letter in 'energy':
    L.append(letter)
print(L)      # ['e', 'n', 'e', 'r', 'g', 'y']

# Shorthand version of the above code using list comprehension
L = [letter for letter in 'energy']
print(L)      # ['e', 'n', 'e', 'r', 'g', 'y']

# c)
L    = ["Practice", "Makes", "us", "100%", "Perfect"]
newL = [x.lower() for x in L if len(x) > 4]

# d) SET
unique_lengths = {len(x) for x in L}

# e) DICTIONARY
L = ["Practice", "Makes", "us", "100%", "Perfect"]
check = list(enumerate(L)) 
# enumerate creates a tuple of list elems with their associated pos in the list
print(check)

location_mappings = {key:val for val,key in enumerate(L)} 
# mapping strings (key) to their locations (val)
print(location_mappings)


#%% Q4 [EXTRA] L10_LAB_Extra_Questions.py 
# Q1. OPERATIONS ON FILES: -------------------------------------------------:
'''
Save the file “USD.csv” from Canvas into your Code folder. This is a daily data 
of GBP/USD and EUR/USD prices over the last 5 years (16/02/2016 – 16/02/2021). 
Your task is to open the file and read lines using each of the three built-in 
functions for reading files. Specifically:
'''

# a)
'''
a) Use read() function to assign contents of the file to a variable allStr. 
   Close the file.
   
   Examine the contents of allStr by printing it. This is one long string of 
   characters. 

   Prove to yourself that allStr is indeed a single string using len(allStr). 

   Access some of the elements and compare output to what you see inside the 
   string in the Variable Explore (the visible part of the values).  
'''
fh = open("USD.csv") # can be without r as reading is default
allStr = fh.read()        # reads data as 1 single long string!
fh.close()
print(allStr)
allStr[1]  # 'D'
allStr[5]  # ','
allStr[22] # '/'

# b)
'''
b)	Read the first row (line) of the file by using readline() command and 
    assign the result to a variable called line1. Note: Since you closed the 
    file after finishing coding part (a), it needs to be re-opened again. 
    If by chance you didn’t close the file, note that the contents of your file 
    are empty. This is because read() function has already read entire file 
    contents. File needs to be re-opened again in order to read its first line.

    What is the type of this variable? 

    Use the print() command to observe what is stored in the variable.
'''
fh = open("USD.csv") 
line1 = fh.readline()     # will read 1 row of excel at a time
fh.close()
print(line1)              # ﻿Date,USDGBP,USDEUR

# c)
'''
c)	Load the entire contents of the file into a list called lines using 
    readlines(). This command results in each element of the list containing 1 
    line of the file. 

    Observe (by printing) the content of the first, second and last elements of 
    this list.
'''
fh = open("USD.csv")
lines = fh.readlines()    # note 'lines' is a list
fh.close()
print(lines[0])           # ﻿Date,USDGBP,USDEUR
print(lines[1])           # 16/02/2016,0.6916,0.89493
print(lines[-1])          # 16/02/2021,0.71872,0.8251


#%% Q2. STRING METHODS -------------------------------------------------------:
myStr      = 'PYTHON'
myStr_lc   = myStr.lower()                   # python
'thon' in myStr_lc                           # True
myStr_swan = myStr_lc.replace('thon','swan') # pyswan
    
# PART 1
line =  '02/01/2013,13412.55,1462.42,3112.26\n' 
# a)
line = line.strip('\n') # equivaletnly line.strip() 
# b)
L = line.split(',')
# c)
date = []; fb = []; amzn = []; brk = [];
# d)
date.append(L[0]) 
fb.append(float(L[1]))    # typecast to float and store Facebook
amzn.append(float(L[2]))  # typecast to float and store Amazon
brk.append(float(L[3]))   # typecast to float and store Berkshire H.
print(date, fb, amzn, brk)

# PART 2
fh = open("stocks.csv") # open file handle that points to dataset 
date = []; fb = []; amzn = []; brk = []
count = 1
for line in fh: # iterating over a file handle iterates over lines of  csv file
    if count == 1:
        pass # do nothing if first iteration (i.e. skip header)
    else:
        L = line.strip('\n').split(',') # you can chain commands through dot
        date.append(L[0]) 
        fb.append(float(L[1]))    
        amzn.append(float(L[2]))    
        brk.append(float(L[3])) 
    count += 1 # incrememt line number by 1
# after the for loop close the file handle:
fh.close()

print(date[0:5])
print(fb[0:5])
print(amzn[0:5])
print(brk[0:5])


