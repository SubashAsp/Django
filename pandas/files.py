import pandas as pd

csv=pd.read_csv('movie.csv')
# print (csv)
# print (csv.head())
# print (csv.head(2))
# print (csv.tail())
# print (csv.tail(1))
# print (csv.tail(2))

# creating a csv file 
# detail={
#     'roll_no': [1, 2, 3],
#     'name': ['Subash', 'Karthi', 'Logu'],
#     'age': [22, 24, 30],
#     'dept': ['IT', 'CSE', 'ECE']
# }
# dataframe=pd.DataFrame(detail)
# print (dataframe)
# dataframe.to_csv('detail.csv', index=False)

# to read a csv file
# d1=pd.read_csv('detail.csv')
# print (d1)
# data=pd.read_csv('detail.csv', header=None)
# print (data)

# to update a csv file
# d=pd.read_csv('detail.csv')
# d['age']=d['age']+1
# d.to_csv('detail.csv', index=False)
# print (d)

# 