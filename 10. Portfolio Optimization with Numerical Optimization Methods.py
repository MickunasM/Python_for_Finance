import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as sco


#%%
#2a)
"""
Consider the dataset with 49 industry portfolios from the previous lectures
Using numerical optimization methods find the optimal mean-variance frontier
(and the corresponding portfolios) for an investor that can only take long-only
positions
Consider target values/grid for the expected return between 0.9% and 1.1%
Take, as initial condition for the optimization, an equally weighted portfolio
across all 49 assets.
"""

df = pd.read_csv("industryPortfolios_1970.csv", dtype = {0:str}, index_col = 0)
rr, cc = df.shape
mu_r = df.mean(axis = 0).values
vcov_r = df.cov().values

#defining the function that we want to maximize
def port_vol(weights):
    aux = np.dot(weights, vcov_r)
    p_vol = (np.dot(aux, weights.T)) ** 0.5
    return p_vol

#setting up the constraints : tuple of 2 dictionaries 
# (each dict contains 2 elements. Keys are: type and fun)
def const1(x):
    output = np.sum(x) - 1
    return output

def const2(x):
    output = np.sum(x * mu_r) - mut
    return output
    
const = ({'type':'eq', 'fun': const1},
         {'type':'eq', 'fun': const2}) 

#more advanced alternative:
#const = ({'type':'eq', 'fun': lambda x: np.sum(x) - 1},
#        {'type':'eq', 'fun': lambda x: np.sum(x * mu_r) - mut})

#setting up the bounds for the portfolio weights
bnds = np.zeros((cc, 2))
bnds[:, 1] = 1
bnds = tuple(bnds)

#more advanced option
#this is list comprehension (a fast way of doing a for loop). List is then typecast to a tuple
#bnds = tuple((0,1) for x in range(cc))

#setting up the initial conditions: create an array with value given by 1. / cc i.e. 0.02040816326530612
# we want to have cc of these entries in the array (we thus multiply cc * [0.02040816] 
# i.e. create a list with cc 0.02040816 elements and then convert it to numpy array)
weights0 = np.array(cc * [1. / cc])

#defining the range of target values for the expected return that we want to consider
gmu = np.linspace(0.9, 1.1, 100)

#find the optimal/minimal volatility for each expected return value (and the corresponding optimal portfolio):
min_vol = []
opt_portf = []
for mut in gmu: # take 1 gmu value at a time
    res = sco.minimize(port_vol, weights0, method = 'SLSQP', bounds = bnds, constraints = const)
    min_vol.append(res['fun'])
    opt_portf.append(res['x'])

#plotting the results
min_vol = np.array(min_vol)
opt_portf = np.array(opt_portf)

plt.figure(figsize = (10, 8))
plt.plot(min_vol, gmu, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.title('Mean-Variance Frontier')
plt.show()


#%%
#2b)
#checking robustness to initial conditions
weights2 = np.zeros(cc)
weights2[0] = 1
min_vol2 = []
opt_portf2 = []
for mut in gmu:
    res = sco.minimize(port_vol, weights2, method = 'SLSQP', bounds = bnds, constraints = const)
    min_vol2.append(res['fun'])
    opt_portf2.append(res['x'])

min_vol2 = np.array(min_vol2)
opt_portf2 = np.array(opt_portf2)

#plot mean-variance frontiers and compare
plt.figure(figsize = (10, 8))
plt.plot(min_vol2, gmu, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.plot(min_vol, gmu,'r')
plt.title('Mean-Variance Frontier')
plt.show()


#%%
##2c)
#hedge fund case: positions between -10% and 10%
gmu_hf = np.linspace(0.9, 1.2, 100)

bnds_hf = np.ones((cc, 2)) * 0.1
bnds_hf[:, 0] = - 0.1   

bnds_hf = tuple(bnds_hf)
#or using the more advanced coding
#bnds_hf = tuple((-0.1, 0.1) for x in range(cc))

min_vol_hf = []
opt_portf_hf = []
for mut in gmu_hf:
    res = sco.minimize(port_vol, weights0, method = 'SLSQP', bounds = bnds_hf, constraints = const)
    min_vol_hf.append(res['fun'])
    opt_portf_hf.append(res['x'])

min_vol_hf = np.array(min_vol_hf)
opt_portf_hf = np.array(opt_portf_hf)

#plot mean-variance frontier
plt.figure(figsize=(10, 8))
plt.plot(min_vol_hf, gmu_hf, 'o')
plt.xlabel('Volatility')
plt.ylabel('Mean')
plt.plot(min_vol, gmu, 'r')
plt.title('Mean-Variance Frontier')
plt.show()



#%%
##2d)
##Portfolio Optimization when penalizing downside risk more heavily
##downside volatility has an extra penalty of 0.5
penalty = 0.5

def port_vol_asym(weights):
    port_ret = np.dot(df.values,weights)
    avg_ret = port_ret.mean(axis = 0)
    #
    p_vol_asym = 0
    for ii in range(rr):
        aux =  (port_ret[ii] - avg_ret)**2
        p_vol_asym += (1 + penalty * (port_ret[ii] < avg_ret)) * aux / rr
    p_vol_asym = p_vol_asym ** 0.5    
    #
    return p_vol_asym

#setting up the constraints : tuple of 2 dictionaries 
# (each dict contains 2 elements. Keys are: type and fun)
const = ({'type':'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type':'eq', 'fun': lambda x: np.sum(x * mu_r) - mut})

#setting up the bounds for the portfolio weights
# this is list comprehension (a fast way of doing a for loop). List is then typecast to a tuple
bnds = tuple((0,1) for x in range(cc))

#setting up the initial conditions: create an array with value given by 1. / cc i.e. 0.02040816326530612
# we want to have cc of these entnries in the array (we thus multiply cc * [0.02040816] 
# i.e. create a list with cc 0.02040816 elements and then convert it to numpy array)
weights0 = np.array(cc * [1. / cc ])

#defining the range of target values for the expected return that we want to consider
gmu = np.linspace(0.9, 1.1, 100)
#gmu = np.linspace(0.9, 1.1, 10)

#find the optimal/minimal volatility for each expected return value (and the corresponding optimal portfolio):
min_vol = []
opt_portf = []
for mut in gmu: # take 1 gmu value at a time
    res = sco.minimize(port_vol_asym, weights0, method = 'SLSQP', bounds = bnds, constraints = const)
    min_vol.append(res['fun'])
    opt_portf.append(res['x'])

min_vol = np.array(min_vol)
opt_portf = np.array(opt_portf)

#plot optimal portfolio frontier
plt.figure(figsize = (10, 8))
plt.plot(min_vol, gmu, 'o')
plt.xlabel('Asymetric Volatility')
plt.ylabel('Mean')
plt.title('optimal Portfolio Frontier')
plt.show()


