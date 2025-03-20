import pandas as pd
import numpy as np

# creating a DataFrame from dictinory
# a = {
#     'movie': ['GOAT', 'GBU', 'DRAGON'],
#     'actor': ['Vijay', 'Ajith', 'Pradeep'],
#     'director': ['VP', 'AR', 'AM']
# }
# a1 = pd.DataFrame(a)
# print (a1)

# creating DataFrame from nested list
# b = [
#     ['GOAT', 'Vijay', 'VP'],
#     ['GBU', 'Ajith', 'AR'],
#     ['DRAGON', 'Pradeep', 'AM']
# ]
# b1 = pd.DataFrame(b, columns=['movies', 'actor', 'director'])
# print (b1)

# creating DataFrame from list of dictionaries
# c = [
#     {'movie':'GOAT','actor':'Vijay','director':'VP'},
#     {'movie':'GBU','actor':'Ajith','director':'AR'},
#     {'movie':'DRAGON','actor':'Pradeep','director':'AM'}
# ]
# c1 = pd.DataFrame(c)
# print (c1)

# creating Dataframe from a numpy array
# d = np.array([
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
# ])
# d1 = pd.DataFrame(d, columns=['a','b','c'])
# print (d1)
# d2 = pd.DataFrame(d)
# print (d2)

# creating Dataframe with custom index
# e = {'movie': ['GOAT','GBU','DRAGON']}
# e1 = pd.DataFrame(e, index=['Vijay','Ajith','Pradeep'])
# print (e1)

# creating an empty DataFrame
# f = pd.DataFrame()
# print (f)

# accessing data in dataframe
# accessing columns
# g = {
#      'movie': ['GOAT', 'GBU', 'DRAGON'],
#      'actor': ['Vijay', 'Ajith', 'Pradeep'],
#      'director': ['VP', 'AR', 'AM']
#  }
# g1 = pd.DataFrame(g)
# print (g1['actor'])

# accessing rows by index
# print (g1.iloc[1])
# print (g1.loc[1])

# accessing multiple rows
# print (g1.iloc[0:2])
# print (g1.loc[0:1])

# accessing both rows and columns
# print (g1.loc[1, ['movie', 'director']])