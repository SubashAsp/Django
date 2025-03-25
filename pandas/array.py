import pandas as pd
import numpy as np

# a=[1, 2, 3, 4, 5]
# a1=pd.array(a)
# # print (a1)
# a2=pd.array(['subash','karthi'])
# # print (a2)
# a3=pd.array([True])
# # print (a3)
# a4=pd.array([1.1, 2.2])
# # print (a4)
# a5=pd.array(pd.to_datetime(['2025-01-01','2025-02-02','2025-03-03']))
# print (a5)

# b=pd.array([1, 2, 3, None, 5])
# print (b)

# array methods 
c=[1, 2, 3, 4, 5]
c1=pd.array(c)
# print (len(c1))
# print (c1.size)
# print (c1)
# print (c1.dtype)
# print (c1.size)
# print (c1.shape)
# print (c1.nbytes)

# mathematical method
# print (c1.sum())
# print (c1.mean())
# print (c1.min())
# print (c1.max())
# print (c1.std())
# print (c1.prod())

# Indexing and slicing 
# print (c1[0])
# print (c1[-1])
# print (c1[0:3])

# Filtering & conditions
# print (c1[c1>2])
# print (c1[c1<=3])
# print (c1[c1%2==0])
# print (c1[c1%2!=0])

# Handling missing values
d=pd.array([1, np.nan, 3, None, 5])
# print (d)
# print (d.isna())
# print (d.fillna(4))

# iterating over an array
# for loop
# for i in c1:
#     print (i)

# square of array
# for i in c1:
#     print (i**2)

# using enumerate()
# for i, j in enumerate(c1):
#     print (f'Label{i}: value{j}')

# using map function
# c2=list(map(lambda x:x**2, c1))
# print (c2)

# c2=list(map(lambda x: int(x**2), c1))
# print (c2)

# c2=pd.array(list(map(lambda x: x**2, c1)))
# print (c2)

# using list comprehension
# c2=pd.array([i**2 for i in c1])
# c2=[int(i**2) for i in c1]
# print (c2)

# using apply
# only appplicable when array is in series
# c2=pd.Series([1, 2, 3, 4, 5])
# c3=c2.apply(lambda x:x**2)
# print (c3)

# conversion bwt pandas and numpy
# np_arr=np.array([1, 2, 3, 4, 5])
# print (np_arr)
# pd_arr=pd.array(np_arr)
# print (pd_arr)

# pandas datetime objects
# d=pd.to_datetime('2025-03-24')
# print (d)
# d=pd.to_datetime(['2025-03-24 10:40:12', '2025-03-23 10:40:14'])
# print (d)

# using different formats
# custom_format=pd.to_datetime('24/03/2025', format='%d/%m/%Y')
# custom_format=pd.to_datetime('24/03/2025')
# print (custom_format)

# different formats
# %Y-%m-%d	2025-03-21
# %d/%m/%Y	21/03/2025
# %m-%d-%Y	03-21-2025
# %B %d, %Y	March 21, 2025

# extracting date
# print (d.year)
# print (d.month)
# print (d.day)
# print (d.weekday())
# print (d.day_name())
# d1=pd.Series(pd.to_datetime(['2025-03-24', '2025-03-25', '2025-03-26']))
# print (d1.dt.weekday)
# print (d1.dt.day_name())

# creating a date range
# d2=pd.date_range(start='2025-03-16', end='2025-03-24')
# print (d2)

# monthly range
# d3=pd.date_range(start='2025-03-24', periods=12, freq='ME')
# print (d3)

# weekly range
# d4=pd.date_range(start='2025-03-24', periods=4, freq="W")
# print (d4)