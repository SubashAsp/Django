import pandas as pd
import numpy as np

# # Creating a series
# a = [1, 2, 3, 4, 5]
# a1 = pd.Series(a)
# print(a1)

# Creating a label(index)
# b = [1, 2, 3, 4, 5]
# b1 = pd.Series(b, index = ['a', 'b', 'c', 'd', 'e'])
# print(b1)

# this raises a ValueError
# b2 = pd.Series(b, index = ['a', 'b', 'c'])
# print(b2)

# # using a key value pair
# c = {'name':'Subash','age':22,'state':'Tamil Nadu'}
# c1 = pd.Series(c)
# print(c1)

# c2 = pd.Series(c, index = ['name','age'])
# print(c2)

# creating a series using scalar values
# c3 = pd.Series(7, index=['s','u','b','a','s','h'])
# print (c3)

# Attributes of series
# d = [10, 20, 30, 40, 50]
# d1 = pd.Series(d, index = ['a', 'b', 'c', 'd', 'e'], name = "Numbers")
# print (d1)
# print (d1.values)
# print (d1.index)
# print (d1.dtype)
# print (d1.name)
# print (d1.size)
# print (d1.shape)

# Methods in series
# Mathematical and Statical methods
# e = [1, 2, 3, 4, 5]
# e1 = pd.Series(e, index = ['v','w','x','y','z'])
# print (e1)
# print (e1.sum())
# print (e1.mean())
# print (e1.max())
# print (e1.min())
# print (e1.std())

# Data cleaning and handling missing values
# f = pd.Series([1,np.nan,3,4,np.nan])
# print (f)
# print (f.dropna())
# print (f.fillna('subash'))
# print (f.isna())
# print (f"Number of missing values: {f.isna().sum()}")
# print (f[f.isna()])
# print (f.isna())

# Sorting & Ordering
# g = [3,1,4,2]
# g1 = pd.Series(g, index=['c','a','d','b'])
# print (g1.sort_values())
# g2 = pd.Series(g, index=['c','d','g','y'])
# print (g2.sort_index())
# using ranking
# h = [10,20,15,30,25]
# h1 = pd.Series(h)
# print (h1)
# print (h1.rank())
# h2 = [1,2,3,5,3,2]
# h3 = pd.Series(h2)
# print (h3.rank())
# print (h3.rank(method='average'))
# print (h3.rank(method='min'))
# print (h3.rank(method='max'))
# print (h3.rank(method='first'))
# print (h3.rank(method='dense'))
# ranking in descending order
# print (h3.rank(ascending=False))
# print (h3.rank(method='dense', ascending=False))
# h4 = [10,20,np.nan,30,15]
# h5 = pd.Series(h4)
# print (h5.rank())

# Accessing Data
# normal indexing (this does not support boolean indexing)
# i = [1, 2, 3, 4, 5]
# i1 = pd.Series(i)
# print (i1)
# print (i1.loc)
# i2 = pd.Series(i, index=['a','b','c','d','e'])
# print (i2['a'])
# print (i2[['a','d']])
# i3 = [1,2,3,4,5]
# i4 = pd.Series(i3)
# print (i4.iloc[0])
# print (i4.iloc[[0,1]])

# performing arithmetic operations
# j = pd.Series([1, 2, 3, 4, 5])
# j1 = pd.Series([10, 20, 30, 40, 50])
# print (j + j1)
# print (j * 2)

# applying functions(apply())
# def square(x):
#     return x * x

# k = [1, 2, 3, 4, 5]
# k1 = pd.Series(k)
# print (k1.apply(square))

# filtering values
# l = [1, 2, 3, 4, 5]
# l1 = pd.Series(l)
# print (l1[l1 > 3])