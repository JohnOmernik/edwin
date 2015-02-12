# Custom per org magics


@register_line_magic
def edwin_custom(line):
    print "\t%edwin_hiveql - Some handy Hive QL tips"

# Some HiveQL Edwin Tips
@register_line_magic
def edwin_hiveql(line):
    print greeting + ", here are some handy HIVE QL statements you asked me to recall for you:"
    print "regexp_replace(cast(fieldname as string), '[^\\u0020-\\u007E]', '*')   -- Remove non printable characters from binary field and display"
    print "reflect('java.net.URLDecoder', 'decode', cast(fieldname as STRING)) - URL Decode using Reflect"


@register_line_magic
def custom(line):
    print "\t%%spark - Run the query and display automagically in a grid in a new window. Useful for large result sets"
    print "\t%%spark_inline - Run the query and display the results in a Dataframe inline. useful for small result sets."
    print "\t%newchat - filename : Type this and it will create a new iPython notebook based on the name of the chat file in the same directory."

# take in a filename, and create a new iPython notebook for that chat.  This is for Chat Translation
@register_line_magic
def newchat(line):
    filename = line
    rf = "readfile(\"" + os.path.basename(filename) + "\")"
    commands = rf
    newNotebook(filename, commands)



# Run spark query, and create a button to display results in another window. We should have edwin keep track of settings for uses on new windows etc. 
@register_line_cell_magic
def spark(line, cell):

    global prev_spark
    global results
    pd.set_option('max_colwidth', 100000)
    pd.set_option('display.max_rows', None)
    out = runSpark(cell)
    prev_spark = out

    df = pd.DataFrame(retSparkJson(out))
    gridhtml = df.to_html()
    if line.find("replacecrlf") >= 0:
        gridhtml = gridhtml.replace("<CR><LF>", "<BR>")
        gridhtml = gridhtml.replace("<CR>", "<BR>")
        gridhtml = gridhtml.replace("<LF>", "<BR>")
        gridhtml = gridhtml.replace("&lt;CR&gt;&lt;LF&gt;", "<BR>")
        gridhtml = gridhtml.replace("&lt;CR&gt;", "<BR>")
        gridhtml = gridhtml.replace("&lt;LF&gt;", "<BR>")

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


