
#These are custom defined functions for your organizations. 

def runSpark(sql):
    return sparkhc.sql(sql).collect()

def retSparkJson(collected):
    return [r.asDict() for r in collected]

def runHive(sql):
  curs = hs2.cursor()
  curs.execute(sql)
  try:
      schema = [unicode(x['columnName'].split('.')[1]) for x in curs.getSchema()]
  except:
      schema = [unicode(x['columnName']) for x in curs.getSchema()]
  myout = [dict(zip(schema, x)) for x in curs.fetch()]
  return myout


#Replaces the <CR><LF> in HTML with <BR> so it displays nice
def replaceHTMLCRLF(instr):
    gridhtml = instr.replace("<CR><LF>", "<BR>")
    gridhtml = gridhtml.replace("<CR>", "<BR>")
    gridhtml = gridhtml.replace("<LF>", "<BR>")
    gridhtml = gridhtml.replace("&lt;CR&gt;&lt;LF&gt;", "<BR>")
    gridhtml = gridhtml.replace("&lt;CR&gt;", "<BR>")
    gridhtml = gridhtml.replace("&lt;LF&gt;", "<BR>")
    return gridhtml
