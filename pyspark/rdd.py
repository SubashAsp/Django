from pyspark.sql import SparkSession

spark=SparkSession.builder .appName('PySpark_Intro') .getOrCreate()
print (spark)

numbers=[1, 2, 3, 4, 5, 6]
rdd=spark.sparkContext.parallelize(numbers)
print (rdd.collect())