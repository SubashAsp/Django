from pyspark.sql import SparkSession

spark=SparkSession.builder .appName('PySpark_Intro') .getOrCreate()
# print (spark)

# numbers=[1, 2, 3, 4, 5, 6]
# rdd=spark.sparkContext.parallelize(numbers)
# print (rdd.collect())

sc=spark.sparkContext
# map(function)
# numbers=[1, 2, 3, 4, 5, 6]
# rdd=sc.parallelize(numbers)
# rdd1=rdd.map(lambda x:x*x)
# print (rdd1.collect())

# filter(function)
# numbers=[1, 2, 3, 4, 5, 6]
# rdd=sc.parallelize(numbers)
# filter_rdd=rdd.filter(lambda x:x>2)
# print (filter_rdd.collect())

# flatmap(function)
# numbers=[1, 2, 3, 4, 5]
# rdd=sc.parallelize(numbers)
# flat_map=rdd.flatMap(lambda x:(x, x*2))
# print (flat_map.collect())

# distinct(function)
# numbers=[1, 2, 3, 4, 5, 2, 4, 6, 5]
# rdd=sc.parallelize(numbers)
# distinct_rdd=rdd.distinct()
# print (distinct_rdd.collect())

# union()
# numbers1=[1, 2, 3, 4, 5]
# numbers2=[6, 7, 8, 9, 0]
# rdd1=sc.parallelize(numbers1)
# rdd2=sc.parallelize(numbers2)
# union_rdd=rdd1.union(rdd2)
# print (union_rdd.collect())

# number1=[1, 2, 3, 4, 5]
# number2=[5, 6, 7, 8, 9]
# rdd1=sc.parallelize(number1)
# rdd2=sc.parallelize(number2)
# union_rdd=rdd1.union(rdd2)
# print (union_rdd.collect())

# reduceByKey(function)-- Aggregate value by key
# dict1=[('A', 1), ('B', 2), ('A', 3), ('B', 4)]
# rdd=sc.parallelize(dict1)
# reduce_rdd=rdd.reduceByKey(lambda x, y:x+y)
# print (reduce_rdd.collect())

# RDD actions
# collect()
# numbers=[1, 2, 3,4 ,5]
# rdd=sc.parallelize(numbers)
# coll=rdd.collect()
# print (coll)
# print (rdd)

# count()
# numbers=[1, 2, 3, 4, 5, 6, 7, 89, 0]
# rdd=sc.parallelize(numbers)
# count=rdd.count()
# print (count)

# first()
# number=[1, 2, 3, 4, 5]
# rdd=sc.parallelize(number)
# first_num=rdd.first()
# print (first_num)

# this method does not work
# first_num=rdd.first(2)
# print (first_num)

# take()
rdd = sc.parallelize([10, 20, 30, 40, 50])
top_3 = rdd.take(3)
print(top_3)  
