#!/usr/bin/python

# Enhancing Data with iPython Notebooks - Edwin

# Core Imports 
from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.display import HTML
from IPython.display import display_html, display

# Third Party Imports
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd
import hashlib
# Data source imports
from pyspark.sql import SQLContext, Row, HiveContext
import pyhs2

# Change how Edwin refers to you. 
greeting = "Sir" # Could be, Maam, could be hey you, we should write a function to change it :) 

# For the magics, it's one thing to just display, but after you run a magic query, it would be nice if you were like "Oh damn, I want those results" well you can with the prev_spark, and other "prev" variables.  We should create one for each magic. 
prev_spark = ""

# Define out your customer data sources here
# This section may need to be moved in a "custom" area for each org.  WE should also add a dictionary item that indicates if the Data Src instantiation was successful
datasrcs = []

datasrc = {}
datasrc['name'] = "Spark Context"
datasrc['desc'] = "Default Connection to local Spark Context"
datasrc['var'] = 'sc'
datasrc['code'] = 'pass'

datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Spark Hive Context"
datasrc['desc'] = "Connection to Spark Cluster Hive Context"
datasrc['var'] = 'sparkhc'
datasrc['code'] = 'sparkhc = HiveContext(sc)'

datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Spark SQL Context"
datasrc['desc'] = "Connection to Spark Cluster SQL Context"
datasrc['var'] = 'sparksql'
datasrc['code'] = 'sparksql = SQLContext(sc)'

datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Hive"
datasrc['desc'] = "Connection to Hive Server2 on Alphaking"
datasrc['var'] = 'hive'
datasrc['code'] = "hive = pyhs2.connect(host='alphaking',port=10000,authMechanism='PLAIN',user='darkness',password='removed',database='default')"

datasrcs.append(datasrc)

# This actual runs all the datasrcs. It should try them and then set a variable in the datasrc if the instantiation was successul. 
for src in datasrcs:
    exec src['code']



#  Generic Helper Functions.  Could use some better documentation and perhaps integration with the %edwin helper
def md5(data):
    return hashlib.md5(data).hexdigest()

def runSpark(sql):
    return sparkhc.sql(sql).collect()

def retSparkJson(collected):
    return [r.asDict() for r in collected]

def runHive(sql):
  curs = hive.cursor()
  curs.execute(sql)
  try:
      schema = [unicode(x['columnName'].split('.')[1]) for x in curs.getSchema()]
  except:
      schema = [unicode(x['columnName']) for x in curs.getSchema()]
  myout = [dict(zip(schema, x)) for x in curs.fetch()]
  return myout

# Magics! 

# Run a spark query. 
@register_cell_magic
def spark(line, cell):
    global prev_spark
    pd.set_option('max_colwidth', 100000)    
    pd.set_option('display.max_rows', None)
    out = runSpark(cell)
    prev_spark = out
    #print type(out)
    df = pd.DataFrame(retSparkJson(out))
    display(df)

# Main Helper
@register_line_magic
def edwin(line):
    print greeting + ", here are some things that may help you:"
    print "Magics:"
    print "%edwin - This is me, please read in a proper Acquired Queens English accent"
    print "%edwin_data - This is also me, reading, in an English Accent, which data sources you have defined," + greeting 
    print "%%spark - Run the following query and display automagically in Pandas Dataframe"
    print ""
    print "Python Functions:"
    print "runSparkDef(sql) : Run the specified SQL using the Spark Hive Context and return a standard Spark Schema RDD"
    print "runSpark(sql) : Run the specified SQL using the Spark hive Context and return a JSON like array of the data useful for Pandas"
    print "runHive(sql) : Run the specified SQL using HiveServer2 and return a JSON like array of the data useful for Pandas etc"
    print "retSparkJson(collected) : Return the collected Spark Schema RDD as JSON. This takes in the result of runSpark"
    print "md5(data) : Return the hexdigest md5"
    print ""
    print "Results of data magics"
    print "prev_spark : Stores the raw (as returned from spark)results of the previous spark Magic command"



# Data Helper
@register_line_magic
def edwin_data(line):
    print "Data stores/Variables Defined defined by you:"
    for x in datasrcs:
        print "%s: Variable: %s - %s" % (x['name'], x['var'], x['desc'])


# Main main MAIN MaIN mAIN
def main():

    print "Enhancing Datascience with iPython Notebooks - EDWIN V1.0"
    print "Hello sir, how may I help you?"

if __name__ == '__main__':
    main()
