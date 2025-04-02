from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark= SparkSession.builder .appName('dataframe').getOrCreate()

# data=[(1, 'subash', 22), (2, 'karthi', 25)]
# data1=spark.createDataFrame(data)
# print (data1.show())
# data1.show()
# print (data1.toPandas())
# index=['no', 'name', 'age']
# data1=spark.createDataFrame(data, index)
# print (data1)
# data1.show()

# data1=spark.createDataFrame(data, schema=index)
# data1.show()

# using all parameters in createDataFrame syntax
# pyspark.sql.SparkSession.createDataFrame(data, schema=None, samplingRatio=None, verifySchema=)True

# using data
data=[('subash', 22), ('karthi', 26), ('deepan', 30)]
# data1=spark.createDataFrame(data)
# data1.show()

# using schema 
index=StructType([
    StructField('name', StringType(), True),
    StructField('age', IntegerType(), True)
])
# data1=spark.createDataFrame(data, schema=index)
# data1.show()

# print (data1.collect())
# may cause memory  issues while handling more number of data

# using samplingRatio 
data2=spark.createDataFrame(data, schema=index, samplingRatio=0.5)
# data2.show()
# data2.printSchema()
# data2=spark.createDataFrame(data, schema=None, samplingRatio=0.5)
# data2.show()

# using verifySchema 
data3=spark.createDataFrame(data, schema=index, verifySchema=False)
# data3.show()

# creating DataFrame from csv
data_csv=spark.read.csv('data.csv', header=True, inferSchema=True)
data_csv.show()