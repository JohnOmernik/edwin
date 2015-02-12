# Edwin level helper functions. These apply universally

#  Generic Helper Functions.  Could use some better documentation and perhaps integration with the %edwin helper
def md5(data):
    return hashlib.md5(data.encode('utf8')).hexdigest()


def results_new_window_click(b):
    global results
    d = b.tooltip.split(':')
    fmd5 = d[0]
    bReplaceCRLF = d[1]
    pd.set_option('max_colwidth', 100000)
    pd.set_option('display.max_rows', None)
    

    df = pd.DataFrame(results[fmd5])
    gridhtml = df.to_html()
    
    if int(bReplaceCRLF) == 1:
        outhtml = replaceHTMLCRLF(gridhtml)
    else:
        outhtml = gridhtml

    window_options = "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=1024, height=800, top=0, left=0"
    base = """var win = window.open("", "&~&", "*~*");
    win.document.body.innerHTML = `%~%`;
    """
    JS = base.replace('%~%', outhtml)
    JS = JS.replace('&~&', fmd5)
    JS = JS.replace('*~*', window_options)

    j = Javascript(JS)
    display(j)
