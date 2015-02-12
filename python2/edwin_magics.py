
# Main Helper edwin
@register_line_magic
def edwin(line):
    print greeting + ", here are some things that may help you:"
    print "Magics:"
    print "%edwin - This is me, please read in a proper Acquired Queens English accent"
    print ""
    print "Some helpful tips from your favorite butler"
    print "  %edwin_data - This is also me, reading, in an English Accent, which data sources you have defined," + greeting
    edwin_custom("") #List out custom Edwins
    print ""
    print "Some helpful Magics:"
    print "  %readfile - Take a path and display the results"
    print "  %%newNotebook - Takes a path and creates a new notebook returning a link. "
    custom("") # List custom Magics
    print ""
    # We need a way to iterate through these files and display them (and functions, and custom variables and custom functions)
    print "Python Functions:"
    print "  runSpark(sql) : Run the specified SQL using the Spark Hive Context return a schema RDD"
    print "  runHive(sql) : Run the specified SQL using HiveServer2 and return a JSON representation"
    print "  retSparkJson(collected) : Return the collected Spark Schema RDD as JSON as outputed by runSpark"
    print "  md5(data) : Return the hexdigest md5"
    print ""
    print "Results of data magics"
    print "  prev_file  : Stores the contents of the previous file read with %readfile"
    print "  prev_spark : Stores the raw (as returned from spark) results of the previous spark magic command"
    print "  prev_hive : Stores the raw (as returned from hive) results of the previous hive magic command"


# Data Helper List out all instantiated items
@register_line_magic
def edwin_data(line):
    print "Data stores/Variables Defined defined by you:"
    for x in datasrcs:
        print "%s: Variable: %s - %s --- Instantiated: %s" % (x['name'], x['var'], x['desc'], x['instantiated'])



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
        title = "# " + filename
        nb['cells'].append(nbf.new_markdown_cell(title))

        for l in cell.split("\n"):
            nb['cells'].append(nbf.new_code_cell(l))
        with open(fname, 'w') as f:
            nbfwrite(nb, f)
    display(FileLink(fname))




#Read a file and output it to the the window
@register_line_magic
def readfile(line):
    global prev_file
    filename = line
    w = open(filename, "rb")
    out = w.read()
    w.close
    prev_file = out
    print out



