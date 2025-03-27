import pandas as pd
import numpy as np

# pandas groupby
# syntax
#   dataframe.groupby('column_name').operation()

data=pd.DataFrame({
    'cat': ['Electronics', 'Electronics', 'Electronics', 'Clothing', 'Clothing', 'Groceries', 'Groceries', 'Groceries'],
    'item': ['Computer', 'Laptop', 'Phone', 'T-Shirt', 'Jeans', 'Flour', 'Rice', 'Oil'],
    'sales': [150000, 100000, 50000, 300, 800, 80, 55, 150]
})
# print (data)

# accessing groups
# data1=data.groupby('cat')
# print (data1)
# print (data1.get_group('Clothing'))

# aggergation functions
# sum_of_data=data.groupby('cat')['sales'].sum()
# print (sum_of_data)

# mean_of_data=data.groupby('cat')['sales'].mean()
# print (mean_of_data)

# deactivating sorting
# mean_of_data=data.groupby('cat', sort=False)['sales'].mean()
# print (mean_of_data)

# alternative method
# def groupby_with_nosort(data, by):
#     return data.groupby(by, sort=False)


# mean_of_data=groupby_with_nosort(data, 'cat')['sales'].mean()
# print (mean_of_data)

# median_of_data=data.groupby('cat')['sales'].median()
# print (median_of_data)

# min_of_data=data.groupby('cat')['sales'].min()
# print (min_of_data)

# max_of_data=data.groupby('cat')['sales'].max()
# print (max_of_data)

# count_of_data=data.groupby('cat')['sales'].count()
# print (count_of_data)

# size_of_data=data.groupby('cat')['sales'].size()
# print (size_of_data)

# std_of_data=data.groupby('cat')['sales'].std()
# print (std_of_data)

# var_of_data=data.groupby('cat')['sales'].var()
# print (var_of_data)

# first_of_data=data.groupby('cat')['sales'].first()
# print (first_of_data)

# last_of_data=data.groupby('cat')['sales'].last()
# print (last_of_data)

# prod_of_data=data.groupby('cat')['sales'].prod()
# print (prod_of_data)

# agg_of_data=data.groupby('cat')['sales'].agg(['sum', 'mean', 'count', 'max', 'min'])
# print (agg_of_data)

# agg_of_data=data.groupby('cat')['sales'].agg(lambda x: x.max()-x.min())
# print (agg_of_data)