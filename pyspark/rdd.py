from pyspark.sql import SparkSession

spark=SparkSession.builder .appName('PySpark_Intro') .getOrCreate()
# print (spark)

# numbers=[1, 2, 3, 4, 5, 6]
# rdd=spark.sparkContext.parallelize(numbers)
# print (rdd.collect())

sc=spark.sparkContext
numbers=[1, 2, 3, 4, 5, 6]
rdd=sc.parallelize(numbers)
rdd1=rdd.map(lambda x:x*x)
print (rdd1.collect())