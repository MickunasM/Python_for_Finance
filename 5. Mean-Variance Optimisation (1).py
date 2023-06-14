#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Consider the dataset in the file "L5_MV_data.csv". 
This dataset has the historical return on the following 2 portfolios:
1) Growth portfolio: portfolio of stocks with the 30% lowest book-market ratio.
2) Value portfolio: portfolio of stocks with the 30% highest book-market ratio.
'''

df = pd.read_csv("L5_MV_data.csv", dtype = {0:str}, index_col = 0)


#%% (a) ----------------------------------------------------------------------: 
'''
    Compute the mean-variance frontier using the special formulas for the 2-asset 
    case (Eq. 3-4). Consider long positions only (i.e. portfolio weights between 
    0% and 100%), and use 100 equally-spaced values for the hypothetical portfolio 
    weights.

    -	Obtain weights, w, at equally spaced intervals between 0 and 1 such that 
        you obtain 100 results. We can use a numpy method called linspace() i.e. 
        linearly spaced numbers. Examine the resulting w below:
'''
    
w = np.linspace(0, 1, 100)
type(w) # numpy.ndarray
print(w)

'''
-	Find mean and std dev of returns on the two portfolios (Value and Growth)
'''

muGrowth = df['Growth'].mean() # df.Growth.mean()  0.9463859649122812
muValue = df['Value'].mean()   # 1.2577982456140337

volGrowth = df['Growth'].std() # 5.3299505348812
volValue = df['Value'].std()   # 7.223677459822241

'''
-	Find correlation between the returns on the 2 portfolios (Value and Growth)
'''

print(df.corr())
corrGV = df.corr().iloc[0, 1]  # 0.8320307112993415 
print(corrGV)

'''
-	For each w find mean and variance of the 2-asset portfolio
-	Print out the top 3 items from the mean and variance found using numpy 
    method round() to 7 decimal places.
'''

mus = w * muGrowth + (1 - w) * muValue
print(mus[0:3].round(7))       # [1.2577982 1.2546527 1.2515071]

vols = ((w * volGrowth) ** 2 + \
        ((1 - w) * volValue) ** 2 + \
        2 * w * volGrowth * (1 - w) * volValue * corrGV) ** 0.5
    
print(vols[0:3].round(7))      # [7.2236775 7.1955678 7.167583]

'''
Examine the plot of the mean-variance frontier with overlaid points for just 
the Value and just the Growth portfolios as red dots.
'''

plt.figure(figsize=(10,8))
plt.plot(vols, mus, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier')
plt.plot(volGrowth, muGrowth, 'r o')
plt.plot(volValue, muValue, 'r o')
plt.show()


#%% (b) ----------------------------------------------------------------------: 
'''
Repeat a) however now allowing for portfolio weights between -100% and +200% 
(produce 100 equally-spaced values).

-	Copy and paste the code you developed to answer a).
-	Adapt the code to create a function which takes w as input.
-	Ensure to create a plot (either inside or outside of the function).
-	Print out the top 3 items from the mean and variance found using numpy 
    method round() to 7 decimal places. 
'''

def MV(w): 
    muGrowth = df['Growth'].mean() 
    muValue = df['Value'].mean()   
    #
    volGrowth = df['Growth'].std() 
    volValue = df['Value'].std()   
    #
    corrGV = df.corr().iloc[0, 1]  
    #
    mus = w * muGrowth + (1 - w) * muValue     
    #
    vols = ((w * volGrowth) ** 2 + \
            ((1 - w) * volValue) ** 2 + \
            2 * w * volGrowth * (1 - w) * volValue * corrGV) ** 0.5 

    
    plt.figure(figsize=(10,8))
    plt.plot(vols, mus, 'o')
    plt.xlabel('Volatility')
    plt.ylabel('Mean')
    plt.title('Mean-Variance Frontier')
    plt.plot(volGrowth, muGrowth, 'r o')
    plt.plot(volValue, muValue, 'r o')
    plt.show()
    #
    '''
    # --- [EXTRA] FANCY PLOTTING (suboptimal part to be coloured red)
    minVol = vols.min()   # min vol
    ind = np.argmin(vols) # index at which vol is minimal
    plt.figure(figsize=(10,8))
    plt.plot(vols[:ind+1], mus[:ind+1], 'o')  # we stop at (stop-1 i.e. at ind)
    plt.plot(vols[ind+1:], mus[ind+1:], 'ro') # start just after ind (ie ind+1)
    plt.xlabel('Volatility')
    plt.ylabel('Mean')
    plt.title('Mean-Variance Frontier')
    plt.plot(volGrowth, muGrowth, 'r o')
    plt.plot(volValue, muValue, 'r o')
    plt.show()
    '''
    # 
    return mus, vols

weights = np.linspace(-1, 2, 100) # result is a numpy array
mus2, vols2 = MV(weights) # store results into variables

print(mus2[0:3].round(7))  # [1.5692105 1.5597738 1.5503371]
print(vols2[0:3].round(7)) # [10.4400944 10.3338514 10.2279879]

# Remember that actual parameters get bound to formal parameters by position.
# Also note that parameter name inside the function (w) do not need to be the 
# same as names outside the function (weights).


#%% (c) ----------------------------------------------------------------------: 

'''
Repeat b) but now assuming that the correlation of the returns of the two 
portfolios is actually i) 0.25; ii) -0.5 (keep all other parameters, namely the 
variances of the two portfolios, unchanged).

-	Copy and paste the code from part b) 
-	Adapt the function to take in another parameter, correlation.
-	Make 2 function calls, one using correlation of 0.25, and another of -0.5. 
    Store results into appropriately named variables. Ensure to plot each case.
    How did the plotted function change?
-	Print out the top 3 items from the mean and variance for each case.
'''

def MV_corr(w, corrGV): 
    muGrowth = df['Growth'].mean() 
    muValue = df['Value'].mean()   
    #
    volGrowth = df['Growth'].std() 
    volValue = df['Value'].std()   
    #
    mus = w * muGrowth + (1 - w) * muValue     
    #
    vols = ((w * volGrowth) ** 2 + \
            ((1 - w) * volValue) ** 2 + \
            2 * w * volGrowth * (1 - w) * volValue * corrGV) ** 0.5 
    # 
    plt.figure(figsize=(10,8))
    plt.plot(vols, mus, 'o')
    plt.xlabel('Volatility')
    plt.ylabel('Mean')
    plt.title('Mean-Variance Frontier')
    plt.plot(volGrowth, muGrowth, 'r o')
    plt.plot(volValue, muValue, 'r o')
    plt.show()
    #
    return mus, vols

weights = np.linspace(-1, 2, 100) # result is a numpy array

correlation = 0.25 
mus3, vols3 = MV_corr(weights, correlation) # store results into variables
print(mus3[0:3].round(7))  # [1.5692105 1.5597738 1.5503371
print(vols3[0:3].round(7)) # [14.0937076 13.8705534 13.6478775]

correlation = -0.5 
mus4, vols4 = MV_corr(weights, correlation) # store results into variables
print(mus4[0:3].round(7))  # [1.5692105 1.5597738 1.5503371]
print(vols4[0:3].round(7)) # [17.7239421 17.398292  17.0728357]

#%% (d) ----------------------------------------------------------------------: 
'''
Repeat b) but using the general formula for the mean-variance frontier (the one
for the multiple assets case, Eq 11 (and constants from Eq 12-15)). Consider 
100 equally-spaced values for the target expected return. 

Note: For the minimum and maximum values of the expected return you can use the 
values obtained in part b) (just to facilitate the comparison between the two 
sets of results). 

-	Obtain the max and min of the means found in b).
'''

max_mu = max(mus2) # 1.5692105263157863
min_mu = min(mus2) # 0.6349736842105287

'''
           Growth      Value
Growth  28.408373  32.034716
Value   32.034716  52.181516
'''

'''
-	Generate 100 equally spaced points using the min and max values found and 
    store the result into a variable called gmu (general mu)
'''

gmu = np.linspace(min_mu, max_mu, 100) # result is a numpy array
# [0.63497368, 0.64441042, 0.65384716, ...]

'''
-	Create a variable vcov_r which obtains variance-covariance matrix of df.
'''

vcov_r = df.cov()


'''
-	Obtain mean of the dataframe and call it mu_r (this should be a vector of 
    2 elements)
'''

mu_r = df.mean() # default is calculating mean down each column (i.e. axis=0)
type(mu_r) # pandas.core.series.Series
mu_r.shape # (2,) i.e. vector

ones = np.ones(2)
type(ones)
ones.shape # (2,) i.e. vector

'''
-	Use equations 12-15 to obtain the constants 
    Hints: np.dot() and np.linalg.inv() will be needed.
'''

temp = np.dot(ones, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
A = np.dot(temp, ones) # 0.03621565578353103
# Equivalently: 
# A2 = np.dot(np.dot(ones, np.linalg.inv(vcov_r)), ones)

temp = np.dot(mu_r, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
B = np.dot(temp, ones) # 0.03179839674662617

temp = np.dot(mu_r, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
C = np.dot(temp, mu_r) # 0.033790068304544486

D = A * C - B ** 2 # 0.00021259144696353935

'''
-	For each mu obtain the corresponding std dev of the mean-variance frontier 
    (using Eq. 11) and call the variable sigma_mvf.
'''

sigma_mvf = ((A * gmu ** 2 -  2 * gmu * B + C) / D) ** 0.5
print(sigma_mvf)
# [6.13808943  6.07534779  6.01447423 ...]

'''
-	Plot the resulting frontier and compare to b).
'''

plt.figure(figsize=(10,8))
plt.plot(sigma_mvf, gmu, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier')
plt.plot(volGrowth, muGrowth, 'r o')
plt.plot(volValue, muValue, 'r o')
plt.show()


#%% (e) ----------------------------------------------------------------------:
'''
Using the general formula for the multiple asset case (Eq. 16), compute the 
portf weights associated with each point on the mvf frontier calculated in d).

-	Obtain variable aux1 which is the dot product of inverted var-cov matrix 
    with vector of ones
-	Obtain variable aux2 which is the dot product of inverted var-cov matrix 
    with vector of mean returns mu_r
-	Obtain the two weights in Eq 16, and call them variables g1 and g2
-	Use Eq. 16 to obtain the portfolio weights w
Hint: np.outer() will be needed.
'''

aux1 = np.dot(np.linalg.inv(vcov_r), ones) # (2,) [0.04416522, -0.00794956]
aux2 = np.dot(np.linalg.inv(vcov_r), mu_r) # (2,) [0.01992824, 0.01187015]

g1 = (C - gmu * B) / D # (100,)
g2 = (gmu * A - B) / D # (100,)

w_mvf = np.outer(g1, aux1) + np.outer(g2, aux2)
print(w_mvf)
'''
array([[ 2.00000000e+00, -1.00000000e+00],
       [ 1.96969697e+00, -9.69696970e-01],
       [ 1.93939394e+00, -9.39393939e-01], 
       ...
'''


#%% (f) ----------------------------------------------------------------------:
'''
Now assume that the investors can also trade a riskless asset with (constant) 
return rf = 0.002728381

Compute the tangency portfolio that defines the new mean-var frontier (Eq. 36).
-	Use Eq.36 to obtain the weights of tangency portfolio and call the var w_tp.
'''

rf = 0.002728381
ex_ret = mu_r - rf
'''
Growth    0.943658
Value     1.255070
'''

aux1 = np.dot(np.linalg.inv(vcov_r), ex_ret) # array([0.01980774, 0.01189184])

temp = np.dot(ones, np.linalg.inv(vcov_r))
aux2 = np.dot(temp, ex_ret) # 0.03169958663948385

w_tp = aux1 / aux2
print(w_tp) # [0.62485807 0.37514193]


# --- Plot tanget to the mv fronteir
'''
-	Produce a plot as per graph from question b) with another plot added to it  
    which contains data pts for the straight line (tangent) to that MV Frontier. 
    Everything is provided below except the slope value and y points defining
    the frontier, which you need to fill in. 
'''
slope = (C - 2 * B * rf + A * rf ** 2) ** 0.5
x = np.linspace(4, 9, 100) # vol
y = x * slope + rf

plt.figure(figsize=(10,8))
plt.plot(vols2, mus2, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier With Riskless Asset')
plt.plot(volGrowth, muGrowth, 'r o')
plt.plot(volValue, muValue, 'r o')
plt.plot(x, y, 'g')
plt.show()

# --- Compute all Sharpe Ratios from (b)
'''
Compare with the portfolio weights with the ones for the portfolio with the 
highest Sharpe Ratio obtained in b). These should be almost identical.
-	Obtain all Sharpe ratios for the mus and sigmas of part b).
-	Hint: np.argmax() will be needed.
'''

SR_all = (mus2 - rf) / vols2 
ind_maxSR = np.argmax(SR_all) # 54
weights[ind_maxSR] # 0.6363636363636365
(1- weights[ind_maxSR]) # 0.36363636363636354

'''
NOTE: The two are slightly different because we only have a fixed set of points 
in our grid in b). If you increase the number of grid points in that 
calculation you will converge to the same answer.
'''

'''
Next, increase the number of grid points for the portfolio weights grid to 1000. 
You will see that the portfolio weights of the maximum Sharpe Ratio portfolio 
are now much closer ones obtained with the formula for the Tangency Portfolio. 
Remember that you need to use the original version of the MV function for this.
'''
weights = np.linspace(-1, 2, 1000) # result is a numpy array
mus2, vols2 = MV(weights) # store results into variables
SR_all = (mus2 - rf) / vols2 
ind_maxSR = np.argmax(SR_all) # 54
weights[ind_maxSR] # 0.6246246246246245
(1- weights[ind_maxSR]) # 0.37537537537537546

'''
Note:
Part b) has the function we want, that we used above to answer the last qn, MV.
Part c) has the same funncion but adjusted MV_corr(). Had we not named it differently
        and had 2 functions called MV, then the last executed function would be
        in memory. 
        So if you wanted the old one you would have had to go back and re-run  
        the function definition nin part b). 
Therefore, as per the solution code, it is best coding practice to always give 
different names to the functions.
'''