# These are the per org imports that need to be run for your enviroment. 

# Setup Spark Enviroment
spark_home = '/opt/mapr/spark/spark-1.2.0-bin-mapr4'
pyspark_submit_args = '--master mesos://hadoopmapr3:5050 --driver-memory 1G --executor-memory 4096M'

# Set the OS ENV for Spark
os.environ['SPARK_HOME'] = spark_home
os.environ['PYSPARK_SUBMIT_ARGS'] = pyspark_submit_args

# Append Spark Paths
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.8.2.1-src.zip'))

# Import Hive and Spark moduels
from pyspark.sql import SQLContext, Row, HiveContext
import pyhs2


#Not sure if this goes here or not... we'll find out. 
execfile(os.path.join(spark_home, 'python/pyspark/shell.py'))





