#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import statsmodels.api as sm

# Load data (parse_dates = True)
data = pd.read_csv("portfolios.csv", dtype = {0:str}, index_col=0) # returns 
bm = pd.read_csv("bookToMarket.csv", dtype = {0:str}, index_col=0) # value (book-to-market)
me = pd.read_csv("marketEquity.csv", dtype = {0:str}, index_col=0) # size (market cap)

# Extract 100 assets 
assets = data.loc[:, 'Asset1':'Asset100'].copy() # 696 x 100

# Obtain rr- number of observations, cc- number of columns (100 assets)
rr, cc = assets.shape


#%% (a) SORT ASSETS ON VALUE AND ON SIZE -------------------------------------:
# part i) sort on value -------------------------------------------------------
'''
Initialise the following variables with relevant index and columns:
'''
assets_sorted = pd.DataFrame(np.nan, index = assets.index, columns =['N/A']*cc)
me_sorted = pd.DataFrame(np.nan, index = assets.index, columns = ['N/A']*cc)

'''
Sort the returns on the 100 assets based on the book-to-market values (sorted 
for each row in ascending order) and store the results into assets_sorted (as 
per previous LAB).

Within the same for loop, also sort the market equity based on the 
book-to-market values and store the result into me_sorted. This allows us to 
keep assets and me aligned following the bm sorting.
'''

for ii in range(rr): # Loop over rows
    # sort book-to-market 1 row at a time and obtain indices 
    inds = bm.iloc[ii, :].argsort() # inds is a pandas Series
    # sort assets based on indices inds of BM row ii
    assets_sorted.iloc[ii, :] = assets.iloc[ii, inds] # 
    # sort me based on indices inds of BM row ii (i.e. same as for assets)
    me_sorted.iloc[ii, :] = me.iloc[ii, inds] # market cap (size)

'''
assets_sorted
196401  2.5834  3.4218   1.2349  2.7648  ...   3.9409   1.5475  1.7217  7.4519
196402  2.0490  2.0159   7.6875  1.4488  ...   2.9068   3.5690  3.2224  2.1957
196403  2.2237  1.7364   0.1374  2.8711  ...  -1.9297  10.2131  8.4639  8.5454
'''

'''
me_sorted
196401    1610.16   3778.00   475.81   3262.01  ...  439.56   61.61   31.44   63.84
196402    1651.85   3912.19   482.26   3353.73  ...  457.54   62.66   31.97   68.69
196403    1683.42   3973.73   517.43    501.84  ...  471.53   64.85   33.05   70.08
'''


# part ii - iv) sort on size --------------------------------------------------
'''
Next we are going to create a data frame of 16 portfolios which will have the 
same number of rows as original data, but only 16 columns. 
'''
n = 16
n1 = round(cc/4)     # 25
n2 = round(cc/(4*4)) # 6
portfolios = pd.DataFrame(np.nan, 
                          index = assets.index, 
                          columns = range(1,n+1)) # 696 x 16 i.e. 16 portfolios
'''
Next a triple nested for loop is required in order to build the portfolios, 
which will be found with the below steps. The first for loop will loop over 
number of observations (rr), the second for loop will loop over [0, 25, 50, 75] 
in order to split it into quarters, and the third for loop will loop over 
[0, 6, 12, 18] to split each quarter in another quarter:

-	create 4 equal-size portfolios based on the previous sort (bottom 25% to top 25%)

-	within each of the previous 4 portfolios sort the assets based on size

-	create an additional 4 equal-size portfolios based on this new sort

-	compute the equal-weighted return on each of these 16 portfolios

First examine the case of obtaining the portfolios.iloc[0, 0] value below:
'''

# TOY EXAMPLE : FILLING IN 1ST ENTRY INTO portfolios
# Look at row 0, and extract first slice of 25 elements from assets_sorted
pSlice = assets_sorted.iloc[0, 0:0+25].copy() # i.e. 0,1,...,24 (25 elements)
# Sort the 25 elements of pSlice based on me_sorted values
ind = me_sorted.iloc[0, 0:0+25].argsort() 
pSlice_sorted = pSlice[ind] # 25x1 pSlice is now sorted according to size
# Obtain first portfolio by taking the mean of first 6 elements
portfolios.iloc[0, 0] = pSlice_sorted[0:0+6].mean() # i.e 0,1,2,3,4,5 (6 elems)
'''
portfolios.iloc[0, 0]
    
port number: 1    2    3    4    5    6   ...   11   12   13   14   15   16
   index     0    1    2....
1963-07 2.0413  NaN  NaN  NaN  NaN  NaN  ...  NaN  NaN  NaN  NaN  NaN  NaN
'''


# Convert the above solution to nested for loops 
for ii in range(rr): # row number
    # SPLIT INTO 4 PORTFOLIOS
    count = 0
    for jj in range(0, cc, n1): # [0, 25, 50, 75]
        pSlice = assets_sorted.iloc[ii, jj:jj+n1].values.copy() # 25; 25; 25; 25
        # sort assets based on size
        ind = me_sorted.iloc[ii, jj:jj+n1].argsort() 
        # sort assets based on ind (on size)
        pSlice_sorted = pSlice[ind] # 25; 25; 25; 25
        # FOR EACH PORTFOLIO, SPLIT INTO 4 PORTFOLIOS AGAIN (equally weighted)
        # n1-1 such that we stop at 23, not 24 (only want 4 portfolios not 5)
        for kk in range(0, n1-1, n2): # [0, 6, 12, 18]
            # print(jj, kk, count)
            portfolios.iloc[ii, count] = pSlice_sorted[kk:kk+n2].mean() 
            if(kk == 18):
                portfolios.iloc[ii, count] = pSlice_sorted[kk:].mean() 
            count += 1 # count will go from 0 to 15 (i.e. 16 elements)

portfolios.to_csv("L8_LAB_a_answer.csv") 
'''
               1         2         3   ...       14        15        16                   
196401  2.041317  0.685550  0.583817  ...  1.814117  1.959350  2.599814
196402  1.492133  1.326333  1.894333  ...  2.204400  3.681883  1.523471
196403  2.141433  1.116617  1.619483  ...  5.893900  6.865417  2.072300
'''


#%% (b) Obtain mean and var of portfolios ------------------------------------:
'''
Report the mean and standard deviation of the 16 portfolios constructed in a) 
This is a single line of code for each.
'''

mean_portfs = portfolios.mean(axis = 0) 
'''
1     1.079711
2     0.974223
3     0.887350
'''
std_portfs = portfolios.std(axis = 0)   
'''
1     6.586738
2     5.779065
3     5.286153
'''

#%% (c) CAPM regression for each portfolio -----------------------------------:
'''
Compute the alpha and beta of the 16 portfolios with respect to the market 
excess return. 
Obtain the p-values of the alphas.
Hint: Adapt previously built capm code.
'''

# Independent variable: market excess return
rf = data['Rf'] # risk free
rm = data['Rm'] # market total return

alphas  = [] # store alpha
betas   = [] # store beta
p_alpha = [] # store p-value for alpha

x = rm - rf # Market excess return 

for ii in range(n):
    X = sm.add_constant(x)           # Add intercept term 
    y = portfolios.iloc[:, ii] - rf # Excess return on asset
    model = sm.OLS(y, X, missing = 'drop') # y.astype(float)
    results = model.fit()
    # obtain estimated coefficients
    alphas.append(results.params.iloc[0]) # extract beta_0 (a.k.a. alpha)
    betas.append(results.params.iloc[1])  # extract beta_1 
    # extract p-value for beta
    p_alpha.append(round(results.pvalues.iloc[0], 4)) 

print(alphas[0:3]) 
'''
[-0.008517841261607484, -0.05690910060088175, -0.11154076019674736]
'''

print(betas[0:3])
'''
[1.3050070540869547, 1.1963397703861314, 1.134976022941425]
'''

print(p_alpha[0:3])
'''
[0.9438, 0.5169, 0.0716]
'''


#%% (d) Obtain value and size factor mimicking portfolios --------------------:
'''
Create a factor-mimicking portfolio for value by going long the portfolios with 
high value and short the portfolios with low value. Create a factor-mimicking 
portfolio for size in the same way.

Hint: e.g. value factor mimicking portfolio:
Obtain variable val_top which contains top 4 portfolios and var_bottom which 
contains bottom 4 portfolios. For each sum up values across rows. Then create 
another variable r_value by taking away the bottom from top values and divide 
by 4.
'''

# Value factor mimicking portfolio (last 4 columns - first 4 columns)
val_top     = portfolios.iloc[:, 12:].sum(axis = 1) # top 4 ports (highest val)
val_bottom  = portfolios.iloc[:, 0:4].sum(axis = 1) # bottom 4 (lowest val)
r_value     = (val_top - val_bottom) / 4
'''
r_value
196401    1.590017
196402    0.768702
196403    2.757981
'''

# Size factor mimicking portfolio 
# (highest size for each bin - lowest size for each bin)
size_top = portfolios.iloc[:, [3,7,11,15]].sum(axis = 1) # top 4 (highest size)
size_bottom =portfolios.iloc[:,[0,4,8,12]].sum(axis=1) # bottom 4 (lowest size)
r_size = (size_top - size_bottom) / 4
'''
r_size
196401   -1.573796
196402    0.859796
196403    0.205236
'''


#%% (e) Regression on 3 factors ----------------------------------------------:
'''
Regress the excess return of each of the 99 assets on a three factor model with 
the factors being: the market excess return, the value factor from d), and the 
size factor from d). (remember to include a constant).
'''

# Indep. variables (factors): market excess return; value factor, size factor.   
res_e = pd.DataFrame(np.nan, index = assets.columns, 
                   columns = ['alpha', 'betaMarket', 'betaValue', 'betaSize', 
                   'p_alpha', 'p_betaMarket', 'p_betaValue', 'p_betaSize'])
x = pd.DataFrame(rm - rf, columns = ['EX']) # Market excess return 
x['VF'] = r_value
x['SF'] = r_size

for ii in range(cc):
    X = sm.add_constant(x)       # Add intercept term 
    y  = assets.iloc[:, ii] - rf # Excess return on asset
    model = sm.OLS(y, X, missing = 'drop')
    results = model.fit()
    # store estimated coefficients
    res_e.iloc[ii, 0:4] = results.params.values
    # store significance 
    res_e.iloc[ii, 4:] = results.pvalues.values

res_e.iloc[0:3, 0:4]
'''
           alpha  betaMarket  betaValue  betaSize
Asset1 -0.600777    1.186600   0.859869 -1.085336
Asset2 -0.028594    0.931770   0.519522 -0.936172
Asset3  0.079785    0.908913   0.588640 -0.982813
'''

res_e.iloc[0:3, 4:]
'''
         p_alpha   p_betaMarket   p_betaValue     p_betaSize
Asset1  0.000008  7.245921e-172  5.383002e-32   2.271847e-85
Asset2  0.682164  1.110077e-264  5.004620e-41  2.361130e-168
Asset3  0.261995  4.184868e-254  4.811528e-49  1.479031e-174
'''

# plot alphas found for regression
plt.figure(figsize = (10, 8))
plt.plot(res_e['alpha'])
plt.legend(['Alphas'])
plt.show()

# plot betas found for regression
plt.figure(figsize = (10, 8))
plt.plot(res_e.iloc[:, 1:4])
plt.legend(['betaMarket', 'betaValue', 'betaSize'])
plt.show()


#%% (f) Regression on 2 factors ----------------------------------------------:
'''
Regress the excess return of each of the 99 assets on a two-factor model with 
the factors being: the market excess return and the value factor from d) 
(remember to include a constant). 
Compare the estimates of alpha (the constant) in parts e) and f).
'''

# Indep. variables (factors): market excess return; value factor.
res_f = pd.DataFrame(np.nan, index = assets.columns, 
                   columns = ['alpha', 'betaMarket', 'betaValue', 
                   'p_alpha', 'p_betaMarket', 'p_betaValue'])
x = pd.DataFrame(rm - rf, columns = ['EX']) # Market excess return 
x['VF'] = r_value

for ii in range(cc):
    X = sm.add_constant(x)       # Add intercept term 
    y  = assets.iloc[:, ii] - rf # Excess return on asset
    model = sm.OLS(y, X, missing = 'drop')
    results = model.fit()
    # store estimated coefficients
    res_f.iloc[ii, 0:3] = results.params.values
    # store significance 
    res_f.iloc[ii, 3:] = results.pvalues.values

round(res_f.iloc[0:3, :], 6)
'''
res_f
           alpha  betaMarket  betaValue   p_alpha  p_betaMarket  p_betaValue
Asset1 -0.666534    1.386721   1.470543  0.000169           0.0          0.0
Asset2 -0.085315    1.104387   1.046267  0.481802           0.0          0.0
Asset3  0.020239    1.090130   1.141628  0.872446           0.0          0.0
'''

# plot alphas found for regression
plt.figure(figsize = (10, 8))
plt.plot(res_f['alpha'])
plt.legend(['Alphas'])
plt.show()

# plot betas found for regression
plt.figure(figsize = (10, 8))
plt.plot(res_f.iloc[:, 1:3])
plt.legend(['betaMarket', 'betaValue'])
plt.show()

# comparing alphas for e) and f)
plt.figure(figsize = (10, 8))
plt.plot(res_e['alpha'])
plt.plot(res_f['alpha'])
plt.legend(['Alphas e)', 'Alphas f)'])
plt.show()


#%% g)
'''
Given values for market risk premium, value factor and size factor, compute:
    expected returns using models in part e)
    expected returns using models in part f)
'''

mrp_e = 0.5   # market risk premium
value_e = 0.2   # value factor
size_e = - 0.1 # size factor

# Note how I split equation on several lines with the \ character
exp_ret_e = res_e['alpha'] + \
            res_e['betaMarket'] * mrp_e + \
            res_e['betaValue'] * value_e + \
            res_e['betaSize'] * size_e
'''
exp_ret_e
Asset1      0.273031
Asset2      0.634812
Asset3      0.750250
...
'''

exp_ret_f = res_f['alpha'] + \
            res_f['betaMarket'] * mrp_e + \
            res_f['betaValue'] * value_e
'''
exp_ret_f
Asset1      0.320935
Asset2      0.676133
Asset3      0.793629
...
'''

plt.figure(figsize = (10, 8))
plt.plot(exp_ret_e)
plt.plot(exp_ret_f)
plt.legend(['ExpRet e)', 'ExpRet f)'])
plt.show()


#%% h) EXTRA; Value-weighted returns ------------------------------------------
'''
Repeat LAB 7 Qb) using value-weighted returns for the 5 portfolios instead of 
equal-weighted returns (where value-weighted returns are returns weighted by 
the relative market cap of each asset), store result into dataframe called 
portfolios_vw.

NOTE: this is referred to as computing value-weighted returns, since we are 
weighting them by the value of each “company”. Not to be confused with the 
concept of the value factor which is based on the book-to-market ratio.

Find mean and standard deviation of each of the newly constructed portfolios. 
'''

n = 20
labels = ['Portf1', 'Portf2', 'Portf3', 'Portf4', 'Portf5']
portfolios_vw = pd.DataFrame(np.nan, index = assets.index, columns = labels)

count = 0
for ii in range(0, cc, n): # range will produce this seq: [0, 20, 40, 60, 80]
# mean along each row, in a vectorised way for all rows in batches of 20 cols
# remember me_sorted was market cap sorted on value
    tot = me_sorted.iloc[:, ii:ii+n].sum(axis=1)
    portfolios_vw.iloc[:, count] = (assets_sorted.iloc[:, ii:ii+n] * 
                                  me_sorted.iloc[:, ii:ii+n]).sum(axis=1) / tot
    count += 1

'''
          Portf1    Portf2    Portf3    Portf4    Portf5
Date                                                    
196401  2.316534  3.332244  1.807151  1.825951  2.765137
196402  1.891069  0.966507  2.187021  2.536570  2.187016
196403  1.547853  0.653939  1.999005  2.701302  3.660255
'''

mu_vw = portfolios_vw.mean(axis=0)
'''
Portf1    0.859612
Portf2    0.773894
Portf3    0.844018
Portf4    0.895697
Portf5    0.985709
'''

sigma_vw = portfolios_vw.std(axis=0)
'''
Portf1    4.498890
Portf2    4.630753
Portf3    4.650433
Portf4    4.869554
Portf5    5.144861
'''

 
# ------------ Alternative 1 (longer way) of doing the above ------------------
portfolios_vw2 = pd.DataFrame(np.nan, index = assets.index, columns = labels)   
for ii in range(rr): # looping over observations
    count = 0
    for jj in range(0, cc, n): # select 20 column entries at a time
        aSlice  = assets_sorted.iloc[ii, jj:jj+n] # vector
        meSlice = me_sorted.iloc[ii, jj:jj+n]
        a_x_me  = np.multiply(aSlice, meSlice) # vector (asset x market cap)
        tot     = meSlice.sum() 
        div     = np.divide(a_x_me, tot) # divide (a*market cap)/tot market cap
        portfolios_vw2.iloc[ii, count] = div.sum() 
        count += 1

'''
portfolios_vw2
          Portf1    Portf2    Portf3    Portf4    Portf5
Date                                                    
196401  2.316534  3.332244  1.807151  1.825951  2.765137
196402  1.891069  0.966507  2.187021  2.536570  2.187016
196403  1.547853  0.653939  1.999005  2.701302  3.660255
'''
#%%