# Custom per org magics


@register_line_magic
def edwin_custom(line):
    print "  %edwin_hiveql - Some handy Hive QL tips"

# Some HiveQL Edwin Tips
@register_line_magic
def edwin_hiveql(line):
    print greeting + ", here are some handy HIVE QL statements you asked me to recall for you:"
    print "regexp_replace(cast(fieldname as string), '[^\\u0020-\\u007E]', '*')   -- Remove non printable characters from binary field and display"
    print "reflect('java.net.URLDecoder', 'decode', cast(fieldname as STRING)) - URL Decode using Reflect"


@register_line_magic
def custom(line):
    print "  %%spark - Run the query and display automagically in a grid in a new window. Useful for large result sets"
    print "    %%spark Options: (put on same line as %%spark):" 
    print "    inline - Display results in notebook rather than button to newwindow"
    print "    replacecrlf - replace <CR><LF> with <BR> in output for easier visualiztion"
    print "  %%hive - Run the query and display automagically in a grid in a new window. Useful for large result sets"
    print "    %%hive Options: (put on same line as %%spark):" 
    print "    inline - Display results in notebook rather than button to newwindow"
    print "    replacecrlf - replace <CR><LF> with <BR> in output for easier visualiztion"
    print "  %newchat - filename : Type this and it will create a new iPython notebook based on source chat file"

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

    jsonresults = retSparkJson(out)
    fmd5 = md5(str(jsonresults))
    results[fmd5] = jsonresults

    if line.find("replacecrlf") >= 0:
        bReplaceCRLF = 1
    else:
        bReplaceCRLF = 0

    if line.find("inline") >= 0:
        bInLine = 1
    else:
        bInLine = 0
    if bInLine == 1:
        df = pd.DataFrame(jsonresults)
        gridhtml = df.to_html()
        if bReplaceCRLF == 1:
            outhtml = replaceHTMLCRLF(gridhtml)
        else:
            outhtml = gridhtml
        display(HTML(outhtml))
    else:
        button = widgets.Button(description="Results")
        button.tooltip = fmd5 + ":" + str(bReplaceCRLF)
        button.on_click(results_new_window_click)
        display(button)




# Run spark query, and create a button to display results in another window. We should have edwin keep track of settings for uses on new windows etc. 
@register_line_cell_magic
def hive(line, cell):

    global prev_hive
    global results
    pd.set_option('max_colwidth', 100000)
    pd.set_option('display.max_rows', None)
    out = runHive(cell)
    prev_hive = out

    jsonresults = out
    fmd5 = md5(str(jsonresults))
    results[fmd5] = jsonresults

    if line.find("replacecrlf") >= 0:
        bReplaceCRLF = 1
    else:
        bReplaceCRLF = 0

    if line.find("inline") >= 0:
        bInLine = 1
    else:
        bInLine = 0
    if bInLine == 1:
        df = pd.DataFrame(jsonresults)
        gridhtml = df.to_html()
        if bReplaceCRLF == 1:
            outhtml = replaceHTMLCRLF(gridhtml)
        else:
            outhtml = gridhtml
        display(HTML(outhtml))
    else:
        button = widgets.Button(description="Results")
        button.tooltip = fmd5 + ":" + str(bReplaceCRLF)
        button.on_click(results_new_window_click)
        display(button)




