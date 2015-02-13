




# Visualization Helper Functions
# These should be setup to take what your data name is, or just use "data" if nothing is provided. These don't actually run the vis (they could) instead 
# we print out the variables and how they work, then we fill the next line so the person can move fast from one to another. 


@register_line_magic
def vis_line(line):
    
    arvals = line.split(' ')
    if len(arvals) == 2:
        datavar = arvals[0]
        xcol = arvals[1]
    if len(arvals) == 1:
        datavar = arvals[0]
        xcol = 'x'
    if len(arvals) == 0:
        datavar = 'datavar'
        xcol = 'x'

    print "Line graphs are simple, I took the liberty of entering some information below, here are some options"
    print "  Specifying the X column helps me understand what you want on the X-Axis"
    print "  You can include the JSON data variable in future calls and I can help craft things easier."
    print ""
    print "In the future, consider '%vis_line $JSONDATA $X_COL"

    myIPython = get_ipython()
    cmd = 'pd.DataFrame(%s).plot(x="%s", figsize=(12, 5))' % (datavar, xcol)
    myIPython.set_next_input(cmd)

@register_line_magic
def vis_bar(line):
    arvals = line.split(' ')
    if len(arvals) == 2:
        datavar = arvals[0]
        xcol = arvals[1]
    if len(arvals) == 1:
        datavar = arvals[0]
        xcol = 'x'
    if len(arvals) == 0:
        datavar = 'datavar'
        xcol = 'x'

    print "Bar graphs are simple, I took the liberty of entering some information below, here are some options"
    print "  Specifying the X column helps me understand what you want on the X-Axis"
    print "  You can include the JSON data variable in future calls and I can help craft things easier."
    print ""
    print "In the future, consider '%vis_line $JSONDATA $X_COL"

    myIPython = get_ipython()
    cmd = 'pd.DataFrame(%s).plot(x="%s", kind="bar", figsize=(12, 5))' % (datavar, xcol)
    myIPython.set_next_input(cmd)








