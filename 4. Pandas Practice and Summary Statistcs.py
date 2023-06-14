#%% IMPORT LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns # another plotting library
import statsmodels.api as sm


#%% PART I) PANDAS PRACTICE
# Explanation of the difference between using dtype and not in read_csv():
df = pd.read_csv("industryPortfolios.csv", dtype = {0:str}, index_col = 0)
df2 = pd.read_csv("industryPortfolios.csv", index_col = 0)

df.index
# Index(['192701', '192702', '192703', Here row names as strings
df2.index
# Int64Index([192701, 192702, 192703, Here row names are numbers

# Extracting a Pandas Series (column)
rf = df['Rf']
rf2 = df2['Rf']

# Remember typically we are allowed to do indexing on a series just like its a
# numpy 1D array, i.e. rf[index] without needing iloc. However, examine this:
rf2[0] # won't work! As indexing is confused by the numbers in the row names
rf2.iloc[0] # works because iloc works on row numbers not row names

rf[0] # works because there is no ambiguity with row labels as they are strings, not numbers
# therefore using dtype is better. 

# -----------------------------------------------------------------------------
#%% Q1
#%% --- 1a)
'''
Load the 'industryPortfolios.csv' dataset into a dataframe df as shown below. 
It reads the first column of dates as a string into index (i.e. row labels).
Otherwise it will read the date in as in as numbers (not date or string).
Examine:
    
-	Create 2 variables: rr and cc which store number of rows and columns of df
    Hint: df.shape command. Result is a tuple, extract its elements. 
    
-	print out row labels and column labels

-	content of data in row 0 column 3 (i.e. Soda, 1927 Jan) and its data’s type
    Hint: iloc
    
-	prove to yourself that data type of np.nan is not the same as data type of 
    None objects
'''
# Explanation of the difference between using dtype and not:
df = pd.read_csv("industryPortfolios.csv", dtype = {0:str}, index_col = 0)

rr, cc = df.shape
# Alternatively
rr = df.shape[0]
cc = df.shape[1]

print(df.index) 
print(df.columns) 
# Check how missing entries were treated: Soda 1st obs was read in as nan:
print(df.iloc[0, 2]) # nan
type(df.iloc[0, 2])  # numpy.float64
# note above is not a NoneType, this is a numpy specific 'not a number - nan' 
# type which is actually recognised as a float, thus it does not break the code
# when we try to work with series that have missing numbers.
print(type(np.nan) == type(None)) # False


#%% --- 1b)
'''
TASK: take away risk free rate (i.e. Rf column) away from every other
column in the dataframe df. 

If we simply try the following, it will not work. The reason for it is that 
broadcasting works on numpy arrays not dataframes such as df:
'''
res = df - df['Rf']
print(res) # all NaNs

df['Agric'] - df['Rf'] 
# works but want to take Rf away from all cols of df, not one col at a time

'''
So we need to convert df into a numpy array and then do broadcasting.

Fist examine the shape of df and Rf columns. Are they compatible for 
broadcasting or do you think we will need to reshape? 
'''

df.shape 
df['Rf'].shape
'''
df is of size (1140,51)
Rf is of size (1140,) 
The shapes are not ready for broadcasting.
Starting from the outer dimension 1140 and 51 do not agree.

We will need to re-shape Rf into a (1140,1) matrix so that we have:
df is of size (1140,51)
Rf is of size (1140,1)
Starting from outer dimensions: 
    1 and 51 (allowed to have 1 as one of the dimensions)
    1140 and 1140 agree
'''

'''
Let's solve the TASK step by step.
STEP1: Convert a dataframe to a numpy array
STEP2: Ensure that numpy array shapes are compatible for broadcasting

Let's begin:
'''

#%% --- 1c)
'''
STEP1:
Extract just the values from the dataframe and store the result into variable 
called data. This extracts just the elements of df, and stores them as a numpy 
array (no longer a dataframe)! Great for us and for our broadcasting ambitions. 

Confirm this by checking:
- datatype of data (should be numpy array)
- data type of the elements contained in data (should be float64)

Next extract Rf as a single column using two approaches:
dictionary like notation df[‘colName’] 
dot notation df.colName

Extract values from column Rf and store result into a variable rf. 
Check the datatype of rf (should be numpy array). Reshape this 
numpy array into a matrix of size (rr,1) i.e. numpy array where rr is the 
number of obs/rows. This will align the 2 arrays (data and rf) for broadcasting.
'''

data = df.values
# what is the data type of variable data:
type(data) # numpy array (i.e. extracted values only from dataframe as ndarray)
# what is the data type of the elements contained in data:
data.dtype # dtype('float64')


df['Rf']
df.Rf

rf = df['Rf'].values
type(rf)
rf = rf.reshape(rr,1)


#%% --- 1d)
'''
STEP2:
We are ready to do broadcasting:
    
Take rf (array, vector shape) away from all cols of data (array, matrix shape). 
The result is a numpy array (call it res) of the same shape as the 
original dataframe df. Check the shape of your resulting array.

You can actually write the above steps of extracting of values, reshaping and 
broadcasting on one line of code! Try to do this.
Hint: remember you can chain operations with the dot notation:
      df.task1.task2.task3 etc executed tasks will be from left to right.
      Roughly it would look as: df.something - df.something
'''

res = data - rf
res.shape

# i.e. we could do this on one line:
res = df.values - df['Rf'].values.reshape(rr,1)


#%% --- 1e)
'''
Create a dataframe with the same row/column labelling as df, which now will 
store the resulting numpy array res as a dataframe, call it df_res.
Great all done with broadcasting!

[EXTRA]:
Next, a quick practice creating and deleting columns:
- Multiply each element of variable rf by 2 and store result as a new column of  
  the df dataframe. Call this new column 'new'.
  Hint: to create a new column in your dataframe df, you simply need to say 
  df['new'] = someValue
- Next delete this newly created column from df.
'''
df_res = pd.DataFrame(res, index = df.index, columns = df.columns)

df['new'] = rf * 2
df.drop(['new'], axis = 1, inplace = True)


# -----------------------------------------------------------------------------
#%% Q2
#%% --- 2a)
'''
Extract all rows and only the following columns from dataframe df: 
    Agric through to Other. Store result into dataframe called monthly_R. 
    Use both approaches to practice how to do this:
-	Firstly using loc
-	Then using iloc
'''

monthly_R = df.loc[:, 'Agric':'Other']
# alternatively all rows (since first part is :), cols by index location (iloc)
monthly_R = df.iloc[:, 0:49]

df.columns.get_loc("Other")

#%% --- 2b)
'''
Create an empty dataframe of size 1x49, which will contain data type np.nan, 
have its single row called ‘alphas’ and column names the same as the original
dataframe df, however only using the 49 portfolios provided (no Rm or Rf).
'''

numInd = 49
alphasAll = pd.DataFrame(np.nan, 
                         index = ['alphas'], 
                         columns = df.columns[:numInd])

#%% --- 2c)
'''
Extract a slice from dataframe df to obtain 12 rows of your choice and all 
columns and store it into results called df_12. Do it in two ways:
    - Create a VIEW on the original dataframe slice
    - Create a copy of the original dataframe slice
'''

n = 12
df_12 = df.iloc[0:12, :]
df_12_copy = df.iloc[0:12, :].copy()


# -----------------------------------------------------------------------------
#%% Q3
# --- 3a)
'''
Use the monthly_R dataframe to calculate the mean of column and store the result 
into mu_monthly_R.
'''
mu_monthly_R = monthly_R.mean(axis = 0) 

# --- 3b) 
'''
Sort the mu_monthly_R in descending order using pandas sort_values() method.
'''
mu_monthly_R.sort_values(ascending = False)

# --- 3c)
'''
Find the cumulative product (down each column) of the dataframe df_12 which you 
found in 2c). Store result into variable called df_12_prod.

Extract the last (12th) row (i.e. this is the last product of values calculated 
going down each column). You should end up with a vector of answers. What is 
the number of elements in your vector?
'''

df_12_prod = df_12.cumprod() # default is axis = 0
x = df_12_prod.iloc[-1, :]
x.shape 



#%% PART II) INDUSTRY PORTFOLIOS 
# Readin data (note: porfolios and market data are already total returns in %)
df = pd.read_csv("industryPortfolios.csv", dtype = {0:str}, index_col = 0)
rr, cc = df.shape
df.head() 


#%% Q1 CALCULATING SUMMARY STATISTICS - MONTHLY (ALL INDUSTRIES) -------------:
# (a) --- Monthly expected excess returns
'''
Compute the average excess return (i.e. return in excess of the risk-free rate) 
over the sample
- First create a numpy array called res, which contains the difference of all
  the columns with the Risk-free column. 
- Next create a dataframe containing res as element values and the same index 
  and column names as df, call this resulting dataframe df_excess_R. 
- As you progress, think about the option of chaining operations on a single line.
'''
res = df.values - df['Rf'].values.reshape(rr,1) 
df_excess_R = pd.DataFrame(res, index = df.index, columns = df.columns)

# all rows (since first part is :), cols by name 
mu_monthly_R = df_excess_R.loc[:, 'Agric':'Other'].mean(axis = 0) 

# alternatively all rows (since first part is :), cols by index location (iloc)
mu_monthly_R = df_excess_R.iloc[:, 0:49].mean(axis = 0) 
print(mu_monthly_R)
'''
Agric    0.661483
Food     0.676203
Soda     0.753990
'''

# (b) --- Sort monthly expected excess returns in descending order
''' 
Sort the industries based on their average excess returns (in descending order, 
which makes most sense since we are dealing with excess returns and the higher 
the better).
'''
mu_monthly_R_sorted = mu_monthly_R.sort_values(ascending = False)
print(mu_monthly_R_sorted)
'''
Aero     1.115755
Paper    1.060037
Fun      0.983764
'''

# (c) --- Volatility of monthly expected excess returns
'''
Compute the volatility of excess returns over the sample.
'''
vol_monthly_R = df_excess_R.loc[:, 'Agric':'Other'].std(axis = 0)
print(vol_monthly_R)
'''
Agric     7.488877
Food      4.758960
Soda      6.232420
'''

# (d) --- Sharpe Ratio of each Industry Portfolio
# No need to take away Rf, as we are dealing with exces returns already
'''
d) Compute the Sharpe ratio.
Note: that there is no need to take away the Risk-free rate in the numerator, 
since we are already dealing with excess returns.
'''

SR = mu_monthly_R / vol_monthly_R 
print(SR)
'''
Agric    0.088329
Food     0.142090
Soda     0.120979
'''

# (e) --- Sort SR
'''
Sort the industries based on their Sharpe ratios.
'''
SR_sorted = SR.sort_values(ascending = False)
print(SR_sorted)
'''
Smoke    0.143390
Drugs    0.143005
Food     0.142090
MedEq    0.137793
Rtail    0.130172
'''


#%% Q2 SUMMARY STATISTICS ANNUAL ---------------------------------------------:
# number of years that we need to create for annual data are:
N = int(rr / 12) # 93 years (int/int = float therefore need to convert to int)

# (a) --- Compute (Compounded) Annual Returns (dfA for Annual)
'''
Compute the series of annual excess returns (remember that you need to compound 
the monthly excess returns).
Hint: solution requires a for loop which will iterate for as many times as 
there are number of years in the dataset. 
'''
# empty dataframe with only col titles
dfA = pd.DataFrame(index = np.arange(N), columns = df.columns) 
t = 12 # want to aggregate over 12 months
count = 0 # needed act as in index to store results into dfA
for ii in range(0, rr, t): # obtain data in steps of t=12
    # obtain a window of 12 obs and find cumulative product
    x = (1 + df_excess_R.iloc[ii:ii+t, :] / 100).cumprod() 
    # only want the final cumulative prod number, i.e. 12th item from x 
    dfA.iloc[count, :] = (x.iloc[-1, :] - 1) * 100 
    count += 1
print(dfA)
'''
        Agric       Food       Soda  ...      Other   Rf         Rm
0   22.512473  37.736808        NaN  ...  20.952063  0.0    28.9716
1   -1.890079  22.624448        NaN  ... -12.389645  0.0  33.438387
2  -20.288277 -18.708046        NaN  ... -64.205415  0.0 -19.183553
'''

# (b)--- Average annual return
'''
Compute the average annual excess return.
'''

mu_annual_R = dfA.loc[:, 'Agric':'Other'].mean(axis = 0) 
print(mu_annual_R)
'''
Agric     8.019422
Food      8.461811
Soda      9.555548
'''


# (c) --- Volatility of annual returns
'''
Compute the volatility of annual excess returns.
'''

vol_annual_R = dfA.loc[:, 'Agric':'Other'].std(axis = 0)
print(vol_annual_R)
'''
Agric    27.816311
Food     17.866300
Soda     23.138846
'''

# (d) --- Sharpe Ratio of each Industry Portfolio
# No need to take away Rf, as we are dealing with exces returns already
'''
Compute the Sharpe ratio based on the moments for annual excess returns.
Note: that there is no need to take away the Risk-free rate in the numerator, 
since we are already dealing with excess returns.
'''
  
SR_annual = mu_annual_R / vol_annual_R 
print(SR_annual)
'''
Agric    0.288299
Food     0.473619
Soda     0.412966
'''

SR_annual_sorted = SR_annual.sort_values(ascending = False)
print(SR_annual_sorted)
'''
Smoke    0.487060
Drugs    0.486840
Food     0.473619
'''


#%% Q3 Portfolios of Different Industries------------------------------------:
# --- 3a) 
'''
Compute the Mean and Volatility of an Equal-Weighted Portfolio of All Industries
Use data from Sep 1965 only (datapoint 511) 

Note: our dataframe df contains NaNs, because the data starts in different mth
for different series. You can check for yourself how many NaNs each column 
contains using the command: 
    df.isnull().sum() 
    The Hlth column contains the most: 510 of them.
Therefore drop all NaN values from the dataframe first, before answering the qn
and store resulting dataframe into a new variable called df_clean.
'''
df_clean = df.dropna()

weights = np.ones(cc)/cc
port_ret = np.dot(df_clean.values,weights)

mean_port_ret = port_ret.mean() # 1.008
std_port_ret = port_ret.std()   # 4.853

mean_port_ret = port_ret[1:].mean() # 1.022
std_port_ret = port_ret[1:].std()   # 4.844

print(df.index)
print(df_clean.index)
# --- 3b)
'''
Compute the Mean and Volatility of the following Portfolio: 
weight on each industry based on last month's relative return: (1+r)/sum((1+r)).
Note: continue working with the df_clean dataframe.
'''
rr, cc = df_clean.shape

port_ret2 = np.zeros(rr-1)
for ii in range(rr-1):
    weight = np.zeros(cc)
    for jj in range(cc):
        weight[jj] = (1+df_clean.iloc[ii,jj]/100)
    sumweight = sum(weight)
    weight = weight/sumweight    
    port_ret2[ii] = np.dot(df_clean.values[ii+1,:],weight)


mean_port_ret2 = port_ret2.mean() # 1.028
std_port_ret2 = port_ret2.std()   # 4.825


#%% Q4 -----------------------------------------------------------------------:
    '''
    For this question consider the first industry only and use the monthly data. 
    Estimate the beta of this industry with respect to the market (CAPM beta) in a 
    regression with a constant, so that you are also estimating CAPM alpha. 

    Report the statistical significance of alpha.
    '''
# (a) --- Industry 1
agric = df['Agric'] # 1st industry only
rf    = df['Rf']    # risk free
rm    = df['Rm']    # market total return

# Single columns are treated as Series, which are named numpy objects.
# calculating rt^i_t - rf_t and rm^i_t - rf_t (Eq 17)
excess_return_industry_y = agric - rf # this is your y for regression
excess_return_market_x   = rm - rf    # this is your x for regression

x = excess_return_market_x   # independent variable
X = sm.add_constant(x)       # add intercept
y = excess_return_industry_y # dependent variable
    
model= sm.OLS(y, X, missing='drop')
results = model.fit()
alpha = results.params.iloc[0] # 0.06817920538979103
beta = results.params.iloc[1]  # 0.9153548657428892
signif = results.pvalues
'''
const     6.871106e-01
0        1.062710e-139
'''

# --- Extra: plotting regressions:
# scatter-plot data
reg_data = pd.DataFrame(x, columns=['x'])
reg_data['y'] = y
sns.regplot(x, y, data=reg_data)


#%% PART III) FINANCIAL DATA SOURCES 
from pandas_datareader import data, wb
# If you dont have the library installed, use IPython magic from Spyder's console:
# %conda install packageName

# Quandl ----------------------------------------------------------------------
aapl = data.DataReader('WIKI/AAPL', 
                       data_source = 'quandl', 
                       start = '2015-01-01', 
                       end = '2021-02-22', 
                       api_key = '!!!your api key!!!') 

# You can omit keywords in order to use poisitional binding
unemp = data.DataReader('FRED/NROUST', 
                        'quandl', 
                        '2000-01-01', 
                        '2021-02-22', 
                        api_key = '!!!your api key!!!')
unemp.plot()


# TIINGO ----------------------------------------------------------------------
# Provide key inside function as argument
aapl = data.DataReader('aapl', 
                       data_source = 'tiingo', 
                       start = '2015-01-01', 
                       end = '2021-02-22', 
                       api_key = '!!!your api key!!!') 

# Set key in environment, then api_key will be set to default None and thus 
# looked up in env automatically 
os.environ['TIINGO_API_KEY'] = '!!!your api key!!!'
aapl = data.DataReader('aapl', 
                       data_source = 'tiingo', 
                       start = '2015-01-01', 
                       end = '2021-02-22') 
aapl.info() # information on the newly created  object
aapl["adjClose"].plot()


# FRED ------------------------------------------------------------------------
# Single series
gdp = data.DataReader('GDP', 'fred', '2000-01-01', '2021-02-22') #quartely data
gdp.loc['2000-01-01'] # access data for a particular date
gdp.plot()

# Multiple series: 
# CPIAUCSL 'consumer price index for all urban consumers: all items'
# CPILFESL 'cPI for all urban consumers: all items less food and energy'
inflation = data.DataReader(['CPIAUCSL', 'CPILFESL'], 
                            'fred', 
                            '2000-01-01', 
                            '2020-11-23') # monthly data



''' FEW OTHER EXAMPLES IF YOU ARE INTERESTED'''
# FAMA/FRENCH -----------------------------------------------------------------
from pandas_datareader.famafrench import get_available_datasets
get_available_datasets()
print(len(get_available_datasets())) # 297 avaiable data sets

portfolio = data.DataReader('5_Industry_Portfolios', 'famafrench') 
# lets take a look at the description of newly uploaded data
print(portfolio['DESCR'])
# portfolio is a dictionary! Keys are numbers between 0-7 contianing values 
# (each value is a DataFrame of data)
type(portfolio[0]) # check what is the type of 'value' stored in this dict: 
# <pandas.core.frame.DataFrame>
# take a look at values stored in key 0
portfolio[0]


# WORLD BANK ------------------------------------------------------------------
# Compare Gross Domestic Products per capita in const dollars in North America:
matches = wb.search('gdp.*capita.*const') # results in a dataframe
matches.iloc[1] # take a look at entry in second row

# To download the NY.GDP.PCAP.KD
gdp_perCap = wb.download(indicator='NY.GDP.PCAP.KD', 
                         country=['US', 'CA', 'MX'], 
                         start=2005, 
                         end=2008)