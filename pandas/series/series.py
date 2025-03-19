import pandas as pd

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

# using a key value pair
# c = {'name':'Subash','age':22,'state':'Tamil Nadu'}
# c1 = pd.Series(c)
# print(c1)

# c2 = pd.Series(c, index = ['name','age'])
# print(c2)

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
e = [1, 2, 3, 4, 5]
e1 = pd.Series(e, index = ['v','w','x','y','z'])
# print (e1)
print (e1.sum())
print (e1.mean())
print (e1.max())
print (e1.min())
print (e1.std())
