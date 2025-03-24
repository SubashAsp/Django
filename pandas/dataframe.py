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

# adding a csv file
# h = pd.read_csv("movie.csv")
# # print (h)
# print (h.head(2))

# creating a csv file in pandas
# i = {
#     'movie': ['GOAT','GBU','DRAGON'],
#     'actor': ['Vijay','Ajith','Pradeep'],
#     'director': ['VP','AR','AM']
# }
# i1 = pd.DataFrame(i)
# i1.to_csv('data.csv')
# print (i1)
# i1.to_csv('data.csv', index=False)
# print (i1)
# i1.to_csv('custom.csv', index=False, header=False)
# print (i1)
# i2 = {
#     'movie': ['Kanguva', 'PS1'],
#     'actor': ['Suriya', 'Karthi'],
#     'director': ['Siva', 'Mani']
# }
# i3 = pd.DataFrame(i2)
# i3.to_csv('data.csv', mode='a', index=False)
# print (i3)

# i4 = pd.read_csv('data.csv')
# print (i4)

# i3.to_csv('data.csv', mode='a', index=False, header=False)

# i4 = pd.read_csv('data.csv')
# print (i4)

# existing_data = pd.read_csv('data.csv')
# new_data = i3
# combined_data = pd.concat([existing_data, new_data]).drop_duplicates()
# combined_data.to_csv('data.csv', index=False, header=False)
# print (combined_data)

# i4 = {
#     'movie': ['Cobra'],
#     'actor': ['Vikram'],
#     'director': ['ANM']
# }
# i5 = pd.DataFrame(i4)
# i5.to_csv('data.csv', mode='a', index=False, header=False)
# print (i5)

# j = {
#      'movie': ['GOAT', 'GBU', 'DRAGON'],
#      'actor': ['Vijay', 'Ajith', 'Pradeep'],
#      'director': ['VP', 'AR', 'AM']
# }
# j1 = pd.DataFrame(j)    
# print (j1)
# print (j1.iloc[0])
# print (j1.iloc[1:3])

# print (j1.loc[0])
# print (j1.loc[:,['actor']])
# print (j1['actor'])
# print (j1[['actor']])

# adding a new column
# j1['md'] = ['U1', 'GVP', 'LJ']
# print (j1)

# k = pd.DataFrame({
#     'name': ['subash', 'karthi', 'logu'],
#     'age': [22, 30, 40]
# })
# k['group'] = ['young' if age < 30 else 'adult' for age in k['age']]
# print (k) 

# using alternative method
# k['group'] = k['age'].apply(lambda age: 'young' if age <30 else 'adult')
# print (k)

# DataFrame.index
l = {
    'a': [10, 20, 30],
    'b': [40, 50, 60]
}
l1 = pd.DataFrame(l)
# print (l1.index)

l2 = pd.DataFrame(l, index=(['a','b','c']))
# print (l2.index)

# DataFrame.columns
# print (l1.columns)
# print (l2.columns)

# print (l1.dtypes)
# l1.info()
