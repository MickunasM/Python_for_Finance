#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Consider the dataset in the file  industryPortfolios_1970.csv. This dataset has 
the historical returns on the 49 industry portfolio that you have used before, 
however now the dataset starts from year 1970 for which all of the observations 
are available.

Note: all equation references refer to the document MV.pdf.
'''

df = pd.read_csv("industryPortfolios_1970.csv", index_col = 0)
rr, cc = df.shape # (602, 49)


#%% (a) ----------------------------------------------------------------------: 
# Computing Mean-Variance Frontier using 100 equally spaced exp returns
'''
Compute the mean-variance frontier, using 100 equally-spaced values for the 
target expected return, with a minimum value of 0.1, and a maximum value of 
2.5 (use Eq 11, and constants from Eqs 12-15). 

-	Obtain the mean of df dataset, mu_r, which is a vector of 49 elements
-	Obtain volatility, sigmas_r
-	Obtain variance-covariance matrix, vcov_r, which is a matrix of 49x49 elems
-	Use numpy linspace to obtain gmu variable with target expected returns
'''

mu_r     = df.mean(axis = 0) # (49,)
sigmas_r = df.std(axis = 0)  # (49,)
vcov_r   = df.cov()          # 49 x 49
# the above variables are all dataframes

n_mu   = 100   # num expected returns that will be considered
min_mu = 0.1
max_mu = 2.5
gmu = np.linspace(min_mu, max_mu, n_mu) # (100,)

'''
-	Calculate A, B, C, D variables using Eq 12-15
'''

def MV(ones, vcov_r, mu_r):
    temp = np.dot(ones, np.linalg.inv(vcov_r))
    A = np.dot(temp, ones)        
    #
    temp = np.dot(mu_r, np.linalg.inv(vcov_r))
    B = np.dot(temp, ones)        
    '''
    # Alternatively:
    temps = np.dot(ones, np.linalg.inv(vcov_r))
    B2 = np.dot(temps, mu_r)
    '''
    # 
    temp = np.dot(mu_r, np.linalg.inv(vcov_r))
    C = np.dot(temp, mu_r) 
    #
    D = A * C - B ** 2            
    #
    return A, B, C, D

ones = np.ones(cc) # (49,)
A, B, C, D = MV(ones, vcov_r, mu_r)

'''
-	Calculate sigma_mvf using Eq 11
-	Plot the MV frontier, overlaid with points for industry portfolios. 
'''

sigma_mvf = ((A * gmu ** 2 -  2 * gmu * B + C) / D) ** 0.5
# [4.13404379, 4.08154322, 4.02995116...
sigma_mvf.shape # (100,)

print(sigma_mvf[0:3])

plt.figure(figsize=(10,8))
plt.plot(sigma_mvf, gmu, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier')
plt.plot(sigmas_r, mu_r, 'ro') # red circles
plt.show()

'''
-	Adapt this code to produce a function which takes as input, vector of 1s of 
    appropriate length (i.e. same as number of industries given by cc) ones, 
    vcov_r, mu_r and outputs values of A, B, C and D.
-	Calculate the values of sigma_mvf using the function you produced.
-	Print out the first 3 sigmas, you should get [4.13404379, 4.08154322, 4.02995116...
'''

#%% (b) ----------------------------------------------------------------------: 
# Computing Portfolio Weights 
'''
Compute the portfolio weights associated with each of points on the mvf 
obtained in a) (use Eq 16)
                                                
-	Design a function which takes as inputs: ones, vcov_r, mu_r, gmu, A, B, C, 
    D and returns weights. 
-	Make a function call and store results into variable called w_mvf. 
-	Print weights for the first 3 rows of the first 3 industries. 
'''
def weights(ones, vcov_r, mu_r, gmu, A, B, C, D):
    aux1 = np.dot(np.linalg.inv(vcov_r), ones) # (49,)
    aux2 = np.dot(np.linalg.inv(vcov_r), mu_r) # (49,) 
    #
    g1 = (C - gmu * B) / D # gamma1 
    g2 = (gmu * A - B) / D # gamma2 
    #
    w_mvf = np.outer(g1, aux1) + np.outer(g2, aux2) 
    #
    return w_mvf, g1, g2

w_mvf, g1, g2 = weights(ones, vcov_r, mu_r, gmu, A, B, C, D) # 100x49
print(w_mvf[0:3, 0:3])
'''
First 3 rows of first 3 industries
[[ 0.16924911  0.04375256 -0.02704423]
 [ 0.16746555  0.04438161 -0.02688616]
 [ 0.16568199  0.04501065 -0.0267281 ]]
'''


#%% (c) ----------------------------------------------------------------------: 
'''
For each set of the portfolio weights identified in b) compute:
-   The largest long position, maxLong (result should be a 100 element vector)
-   The largest short position, maxShort (result should be a 100 elem vector)
'''
maxLong  = w_mvf.max(axis = 1)
print(maxLong[0:3])  # [0.59343514 0.58373814 0.57404114]

maxShort = w_mvf.min(axis = 1)
print(maxShort[0:3]) # [-0.32876157 -0.32530515 -0.32184873]

'''
For each of the two series above report:
-	The average (i.e. the average for maxLong and the average for maxShort)
-	The maximum (i.e. the max of maxLong and the max of maxShort)
'''
# series of max and min find 
av_maxLong   = maxLong.mean()   # 0.4029243787595149
av_maxShort  = maxShort.mean()  # -0.32798058793063156

abs_maxLong  = np.max(maxLong)  # 0.5934351418819535
abs_maxShort = np.min(maxShort) # -0.6003113354907658


#%% (d) ----------------------------------------------------------------------: 
'''
Now assume that the investors can also trade a riskless asset with a (constant) 
return rf = 0.002728381.

Compute the tangency portfolio (Eq 36) that defines the new mean-var frontier.
-	Create excess return variable, ex_ret
-	Write a function to compute the weights, w_tp
-	Print out the first 3 values of w_tp
-	Obtain a plot containing the MV frontier (using sigma_mvf & gmu variables), 
    tangent line (obtained by calculating the slope, and creating equation of a 
    line using slope and rf) and the industries (plotted as red dots).
'''
# Tangency Portfolio With Riskless Asset
rf     = 0.002728381
ex_ret = mu_r - rf

def MV_with_riskless(ones, vcov_r, ex_ret):
    aux1 = np.dot(np.linalg.inv(vcov_r), ex_ret) # (49,) 
    #
    temp = np.dot(ones, np.linalg.inv(vcov_r))
    aux2 = np.dot(temp, ex_ret) # (49,) 
    #
    w_tp  = aux1 / aux2 # (49,) (element-wise division)
    #
    return w_tp
    
w_tp = MV_with_riskless(ones, vcov_r, ex_ret) # (49,)
# weights of tangency portfolio
#  array([ 0.03823727,  0.08995938, -0.01543373,  ...

# --- Plot tanget to the mv fronteir found in a)
slope = (C - 2 * B * rf + A * rf ** 2) ** 0.5
x = np.linspace(2, 7, 100) # vol
y = x * slope + rf

plt.figure(figsize=(10,8))
plt.plot(sigma_mvf, gmu, 'o')
plt.plot(x, y, 'g')
plt.plot(sigmas_r, mu_r, 'r o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier With Riskless Asset')
plt.show()

'''
Compare with the portfolio with the highest Sharpe Ratio obtained in b).
-	Obtain all SR using gmu and sigma_mvf variables
-	Use numpy argmax to find index, ind_maxSR, corresponding to the highest SR
-	Find values contained inside w_mvf indexed by the ind_maxSR these should be 
    very close to the values found in w_tp.
'''
# --- Compute all Sharpe Ratios from (b)
SR_all = (gmu - rf) / sigma_mvf 
ind_maxSR = np.argmax(SR_all) # 73
ans1 = w_mvf[ind_maxSR]       # (49,)
# array([0.0390493 ,  0.08967298, -0.01550569 ...

# Note that the above answer is very close to the answer found for weights of 
# the tangency portfolio w_tp 49x1, where first 3 weights were:
# array([ 0.03823727,  0.08995938, -0.01543373

#%% (e) ----------------------------------------------------------------------: 
'''
Repeat b) using the “shrinkage” procedure for variance-covariance matrix 
discussed in the notes (with weights of 0.5 on both the original matrix and the 
“variance-only matrix”). Eq 17 

-	Obtain a new var-covariance matrix using Eq 17 and store result to vcov_sh
    Hints: useful functions to help you numpy diag() to extract a diagonal from 
    a matrix (documentation here), numpy eye() to create an identity matrix i.e
    1 on diagonal and 0s on off diagonal (documentation here).  
-	Make a call to the function created in part a) using the shrinkage var-cov 
    matrix. 
-	Make a call to the function created in part b) using the found constants 
    A-D and the shrinkage var-cov matrix.
-	Print weights for the first 3 rows of the first 3 industries.
'''
diag    = np.diag(vcov_r)   # vector of varainces
H       = np.eye(cc) * diag
theta   = 0.5
vcov_sh = (1 - theta) * vcov_r + theta * H

# funciton from part a)
A, B, C, D = MV(ones, vcov_sh, mu_r)
# function from part b)
w_mvf_sh, _, _ = weights(ones, vcov_sh, mu_r, gmu, A, B, C, D)
#                  ones, vcov_r, mu_r, gmu, A, B, C, D
print(w_mvf_sh[0:3, 0:3])
'''
[[ 0.08594833  0.06637507 -0.01951077]
 [ 0.08500824  0.06749159 -0.01848828]
 [ 0.08406815  0.06860811 -0.01746579]]
'''


'''
-   Compare the portfolio positions with the results obtained in c).
'''
# ---
maxLong_sh  = w_mvf_sh.max(axis = 1)
print(maxLong_sh[0:3])  # [0.42998786 0.42503271 0.42007756]
 
maxShort_sh = w_mvf_sh.min(axis = 1)
print(maxShort_sh[0:3]) # [-0.23106955 -0.22388591 -0.21670227]
 
# series of max and min find 
av_maxLong_sh   = maxLong_sh.mean()   # 0.3078410844574266
av_maxShort_sh  = maxShort_sh.mean()  # -0.23424353388307625
 
abs_maxLong_sh  = np.max(maxLong_sh)  # 0.4801107475855942
abs_maxShort_sh = np.min(maxShort_sh) # -0.592105375329692


# --- [EXTRA]

'''
-	[EXTRA] Obtain a plot of the MV frontier from part a) overlaid with the new 
    MV frontier found with the shrinkage var-cov approach and the industry 
    portfolios as red dots. You only need to obtain: sigma_mvf_sh
'''
# Obtain the plot
sigma_mvf_sh = ((A * gmu ** 2 -  2 * gmu * B + C) / D) ** 0.5

plt.figure(figsize=(10,8))
plt.plot(sigma_mvf_sh, gmu, 'g o')
plt.plot(sigmas_r, mu_r, 'r o')
plt.plot(sigma_mvf, gmu, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier')
plt.legend(['Shrinkage', 'Industries', 'Original'])
plt.show()


#%% (f) ----------------------------------------------------------------------: 
#%% (f) OPTION 1
'''
Consider the case of a long-only investor (e.g. a Mutual Fund) who therefore 
requires a portfolio without any short positions. Let’s consider 2 experiments 
to try to obtain an optimal portfolio for this investor.

Note: In both cases you should compute the optimal portfolio only for one value 
of the target expected return (you can always add an outer loop to compute for 
all if you are curious about the results). Consider the value of expected 
return in position 50 of the vector that you have used before (indexed by 49).
Set up:
'''
# Consider only 1 target expected return located in position 50 of gmu
mut = 49 # mu at time step t
gmu_lo = gmu[mut] #  1.287878787878788 target expected return at t=50
w_mvf_cap = w_mvf[mut, :].copy() # (49,) extract a row from w_mvf_cap

'''
To do:
Remove all assets that have negative/short positions (i.e. their portfolio 
weight becomes zero) and re-compute the mean-variance frontier using only the 
remaining assets.

- Obtain a boolean vector called cond, which would contain True/False results 
  to indicate where w_mvf_cap is positive.
'''
# Long only: find elements of the 50th row of w_mvf, which are positive
cond = w_mvf_cap > 0 # (49,)

'''
Code provided:
- We create a copy of the returns for which the condition is True such that we  
  can work on the dataframe without affecting the original returns data, using: 
  ret_lo = df.iloc[:, cond].copy()
  Note: here we selected all rows, but only the columns (industries), for which 
  the condition was true. And then took a copy of that result and assigned to a 
  new var.
'''
# Obtain returns for long only positions
ret_lo = df.iloc[:, cond].copy() # (624, 29) (prev. we had 49 industries, now 29)
rr_lo, cc_lo = ret_lo.shape      # (624, 29)

'''
To do:
- Obtain number of rows and cols of the new dataframe; call them rr_lo, cc_lo
- Obtain the new var-cov matrix, call it vcov_r_lo, and new mean returns vec, 
  call it mu_r_lo
- Create new vector of ones, using the correct number of industries and call it 
  ones_lo
'''
vcov_r_lo = ret_lo.cov()         # 29x29 new var-cov matrix
mu_r_lo = ret_lo.mean(axis = 0)  # (29,) means column-wise for the reduced data
ones_lo = np.ones(cc_lo) # (29,)

'''
To do:
- Make a function call to the appropriate function to obtain constants 
  A, B, C, D and call the result A_lo, B_lo, C_lo, D_lo. 
- Make a function call to the function weights(parameters) ensuring to pass 
  gmu_lo (corresponding to mut only) to obtain weights, call them w_mvf_lo1
- Print out the first 3 weights 
'''
# --- recompute using functions MV and weights
A_lo, B_lo, C_lo, D_lo = MV(ones_lo, vcov_r_lo, mu_r_lo)
w_mvf_lo1, _, _ = weights(ones_lo, vcov_r_lo, mu_r_lo, gmu_lo, A_lo, B_lo, C_lo, D_lo) 
w_mvf_lo1.shape # (1,29) i.e. a matrix with a single row of 29 elements
# array([[0.02903268,  0.13630675,  0.12673855, ...


#%% (f) OPTION 2
'''
-   Remove all assets that have negative/short positions (i.e. their portfolio 
    weight becomes zero) and re-scale the remaining portfolio appropriately.
    Hint: Use the condition cond to select elements of w_mvf_cap with boolean 
    indexing and sum up all of the weights. 
-	Re-scale portfolio to obtain w_mvf_lo2
'''
w_mvf_cap = w_mvf[mut, :].copy() # (49,)

# sum up weights which are positive
totalw  = w_mvf_cap[cond].sum() # 2.4964169929188156

w_mvf_lo2 = w_mvf_cap[cond] / totalw
# array([0.03278888, 0.02987316, 0.02783649, ...


#%% [EXTRA] (g) --------------------------------------------------------------: 
'''
Now consider a Hedge Fund that can take short positions but does not want to 
have very high exposures (long or short) to any particular asset. In c) we saw 
how the portfolio weights can be decreased through the “covariance shrinkage 
method” now we will impose portfolio constraints directly. 

More precisely the Hedge Fund wants portfolio weights between -25% and +25%:
•	All long positions smaller or equal to 25%. 
•	All short positions smaller or equal to 25% (i.e. values can’t be more 
    negative than -25%).

The procedure that we are going to implement is as follows:
•	Set all positions in excess of 25% to 25%
•	Set all positions below -25% to -25%
•	Re-scale the rest of the portfolio appropriately 

Note: Just as in e), perform the calculations only for one value of the target 
expected return (the one in position 50 of the grid used before). 

Hint: you will require a while loop, since after each re-scale some weights 
might move to beyond the allowed limits. 
Useful function: numpy where
'''

w_cap   = 0.25
w_floor = -0.25

w_mvf_cap = w_mvf[mut, :].copy() # 49x1
# array([0.09137018,  0.08324517, -0.02154268, ...

cond1 = np.where(w_mvf_cap > 0.25)  # array containig a sinlge element (tuple)
cond2 = np.where(w_mvf_cap < -0.25) # array containig a sinlge element (tuple)

count = 0 # let's keep track of how many loops were necessary
# cond1[0] extract array with indecies of where 
while len(cond1[0]) > 0 or len(cond2[0]) > 0:
    w_mvf_cap[cond1] = 0.25
    w_mvf_cap[cond2] = -0.25
    #
    totalw  = w_mvf_cap.sum() 
    w_mvf_cap = w_mvf_cap / totalw
    #
    cond1 = np.where(w_mvf_cap > 0.25)
    cond2 = np.where(w_mvf_cap < -0.25)
    # count number of iterations
    count += 1

print(count) # looped 28 times
print(w_mvf_cap[0:3])
# [0.09137018  0.08324517 -0.02154268]