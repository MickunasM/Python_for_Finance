import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%%
##1a)
"""
Consider the data set with the Growth and Value Portfolios from Lecture 5
Suppose the asset manager is targeting an expected return of 1.5%.
i) What portfolio should the asset manager buy?
ii) What return volatility should the asset manager expect for this portfolio?
"""
df = pd.read_csv("L5_MV_data.csv", dtype = {0:str}, index_col = 0)

def MV(vcov_r, mu_r, mu):
    ones = np.ones(2)
    
    temp = np.dot(ones, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
    A = np.dot(temp, ones) 
    
    temp = np.dot(mu_r, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
    B = np.dot(temp, ones) 
    
    temp = np.dot(mu_r, np.linalg.inv(vcov_r)) # (2,) x (2,2) = (2,)
    C = np.dot(temp, mu_r) 
    
    D = A * C - B ** 2 
    
#    sigma = ((A * mu ** 2 -  2 * mu * B + C) / D) ** 0.5
    
    aux1 = np.dot(np.linalg.inv(vcov_r), ones) # (2,) 
    aux2 = np.dot(np.linalg.inv(vcov_r), mu_r) # (2,) 
    g1 = (C - mu * B) / D 
    g2 = (mu * A - B) / D 
    
    w = g1*aux1 + g2*aux2
    
    return w


vcov_r = df.cov()
mu_r = df.mean() # default is calculating mean down each column (i.e. axis=0)
mu0 = 1.5

w = MV(vcov_r, mu_r, mu0)


#%%
##1b)
"""
Simulate 10000 returns for Value and Growth from (independent) normal 
distributions with their historical means and volatilities.

For Growth:
    Mean: 0.946% 
    Volatility: 5.33%
For Value:
    Mean: 1.258%
    Volatility: 7.22%
"""
np.random.seed(1234) 

rr, cc = df.shape # cc = 2 i.e. number of assets (i.e. Value and Growth)
nsim = 10000


mu = mu_r.values
std = np.diag(vcov_r) ** 0.5 # numpy array

ret = np.zeros([nsim,cc])


for ii in range(cc):
    ret[:, ii] = np.random.normal(mu[ii], std[ii], nsim)

print(ret.mean(axis = 0)) # 1.0323392  1.24217841
print(ret.std(axis = 0)) # 5.30425967 7.181022


#%%
##1c)
"""
Improving the previous simulations by simulating only 5000 draws and setting 
the other 5000 be the symmetric of those first ones.
"""
#improving simulations
np.random.seed(1234) 
n = int(nsim / 2)
ret2 = np.zeros([nsim, cc])

for ii in range(cc):
    ret2[:n,ii] = np.random.normal(0, std[ii], n)
    ret2[n:,ii] = - ret2[:n, ii]
    ret2[:, ii] = ret2[:, ii] + mu[ii]

print(ret2.mean(axis = 0)) # 0.94638596 1.25779825
print(ret2.std(axis = 0)) # 5.28769384 7.21312201

# We note that the mean is now correct.


#%%
##1d)
"""
Incorporate the historical correlation between Value and Growth (0.832) in the 
simulations use the formula provided in the slides.
"""
#incorporating correlation
np.random.seed(1234) 
ret3 = np.zeros([nsim,cc])


ret3[:n, :] = np.random.multivariate_normal([0,0], vcov_r, n)
ret3[n:, :] = - ret3[:n, :] 

ret3.shape
mu.shape

# add respective mean to each column
# option 1: vectorised way
ret3 = ret3 + mu

# checking the results
print(ret3.mean(axis = 0)) # [0.94638596 1.25779825]
print(ret3.std(axis = 0)) # [5.2833195 7.1753924]
sim_cov = np.cov(ret3.T)
print(sim_cov)
# [[27.91625653 31.45974574]
# [31.45974574 51.49140521]]
print(vcov_r)
# Growth  28.408373  32.034716
# Value   32.034716  52.181516

#NOTE: if we had used:
np.random.seed(1234) 
ret3b = np.random.multivariate_normal(mu, vcov_r, nsim)
# then the mean would be off again:
print(ret3b.mean(axis = 0)) # [0.9066054, 1.24405895]
print(ret3b.std(axis = 0)) # [5.32278383, 7.18360729]


#%%
##1e)
# ------------- FIND PROBABILITY OF NEGATIVE PORTFOLIO RETURN -----------------
"""
Using the simulations from 1d) compute:
    The probability of obtaining a negative portfolio return.
    The 10th percentile of the distribution of returns.
"""

"""

Consider 2 alternative ways of performing this computation:
- version 1: combining a foor loop and an element-by-element if condition 
- version 2: using vectorization and a boolean operator on a vector

"""
'''
# option 2: using a for loop
for ii in range(cc):
    ret3[:,ii] = ret3[:,ii] + mu[ii] 
'''
# --- WAY 1) using for loops
count = 0
rp3 = np.zeros(nsim)
for ii in range(nsim):
    rp3[ii] = ret3[ii, 0] * w[0] + ret3[ii, 1] * w[1]
    if rp3[ii] < 0:
        count += 1
'''
rp3
array([-21.80128626,   3.18698037,   2.26254284, ..., -13.25338762,
        -7.39410143,   1.07119892])
'''
prob_neg_ret3 = count / nsim # 0.4388


# --- WAY 2) using vectorization
rp3_v2 = (ret3 * w).sum(axis = 1)
'''
array([-21.80128626,   3.18698037,   2.26254284, ..., -13.25338762,
        -7.39410143,   1.07119892])
'''
count_v2 = len(np.where(rp3_v2 < 0)[0])

prob_neg_ret3_v2 = count_v2 / nsim # 0.4388


# ------------------------ FINDING 10TH PERCENTILE-----------------------------
rp3_sorted = np.sort(rp3)
ret3_10_percentile = rp3_sorted[int(0.1 * nsim)] # -10.84343963517819


#%%
##1f)[EXTRA]
'''
Plotting a histogram with the distribution of the portfolio returns.
Review np.histogram documentation online.
'''
#plotting a histogram
hist, bin_edges = np.histogram(rp3_sorted, bins = 100)

plt.figure(figsize = (10, 8))
plt.plot(bin_edges[:-1], hist)
plt.legend(['Probability'])
plt.show()

