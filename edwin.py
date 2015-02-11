#!/usr/bin/python

# Enhancing Data with iPython Notebooks - Edwin

# Core Imports 
from IPython.core.magic import (register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.nbformat import v4 as nbf
from IPython.nbformat import write as nbfwrite
from IPython.core.display import HTML
from IPython.display import display_html, display, Javascript, FileLink, FileLinks
from IPython.html import widgets # Widget definitions


# Third Party Imports
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd
import hashlib
import os
# Data source imports
try:
    from pyspark.sql import SQLContext, Row, HiveContext
    import pyhs2
except:
    pass

# Change how Edwin refers to you. 
greeting = "Sir" # Could be, Maam, could be hey you, we should write a function to change it :) 

# edwin's location
edwin_loc = os.path.dirname(os.path.realpath(__file__))

# This is where the results are stored for the magics, this may get large, we should probably keep tabs on that. 
results = {}

# For the magics, it's one thing to just display, but after you run a magic query, it would be nice if you were like "Oh damn, I want those results" well you can with the prev_spark, and other "prev" variables.  We should create one for each magic. 
prev_spark = ""
prev_file = ""
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
    try:
        exec src['code']
    except:
        pass


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


# Run spark query, and create a button to display results in another window. We should have edwin keep track of settings for uses on new windows etc. 
@register_cell_magic
def spark(line, cell):
    global prev_spark
    global results
    pd.set_option('max_colwidth', 100000)
    pd.set_option('display.max_rows', None)
    out = runSpark(cell)
    prev_spark = out
    df = pd.DataFrame(retSparkJson(out))
    gridhtml = df.to_html()
    window_options = "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=780, height=200, top=0, left=0"
    fmd5 = md5(gridhtml)
    base = """var win = window.open("", "&~&", "*~*");
    win.document.body.innerHTML = `%~%`;
    """
    JS = base.replace('%~%', gridhtml)
    JS = JS.replace('&~&', fmd5)
    JS = JS.replace('*~*', window_options)
    results[fmd5] = JS
    
    
    button = widgets.Button(description="Results")
    button.tooltip = fmd5
    button.on_click(display_spark_results)

    display(button)



# Run a spark query. and display in line (old method) 
@register_cell_magic
def spark_inline(line, cell):
    global prev_spark
    pd.set_option('max_colwidth', 100000)    
    pd.set_option('display.max_rows', None)
    out = runSpark(cell)
    prev_spark = out
    #print type(out)
    df = pd.DataFrame(retSparkJson(out))
    display(df)



@register_line_magic
def readfile(line):
    filename = line
    w = open(filename, "rb")
    out = w.read()
    w.close
    prev_file = out
    print out



def display_spark_results(b):
    global results
    fmd5 = b.tooltip
    j = Javascript(results[fmd5])
    display(j)

# Main Helper
@register_line_magic
def edwin(line):
    print greeting + ", here are some things that may help you:"
    print "Magics:"
    print "%edwin - This is me, please read in a proper Acquired Queens English accent"
    print "%edwin_data - This is also me, reading, in an English Accent, which data sources you have defined," + greeting
    print "%%spark - Run the following query and display automagically in a grid in a new window. Useful for large result sets"
    print "%%spark_inline - Run the following query and display the results in a Dataframe inline. useful for small result sets."
    print "%readfile - Take a path and display the results"
    print "%%newNotebook - Takes a path and creates a new notebook returning a link. "
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

# line is the name (withtout the ipynb extension cell is any additional lines (other than edwin and the title to add)
@register_line_cell_magic
def newNotebook(line, cell):
    name = line
    filename = os.path.basename(name)
    dirname = os.path.dirname(name)
    
    fname = dirname + '/' + filename + ".ipynb"

    if os.path.exists(fname):
        print "File Exists, not creating. Here is a link!"
    else:
        nb = nbf.new_notebook()
        edwin = "%run -i " + edwin_loc + "/edwin.py"
        title = "# " + filename
        nb['cells'].append(nbf.new_code_cell(edwin))
        nb['cells'].append(nbf.new_markdown_cell(title))
        
        for l in cell.split("\n"):
            nb['cells'].append(nbf.new_code_cell(l))
        with open(fname, 'w') as f:
            nbfwrite(nb, f)
    display(FileLink(fname))

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
    print "I am running from: %s" % edwin_loc

if __name__ == '__main__':
    main()
