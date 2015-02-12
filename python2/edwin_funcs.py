# Edwin level helper functions. These apply universally

#  Generic Helper Functions.  Could use some better documentation and perhaps integration with the %edwin helper
def md5(data):
    return hashlib.md5(data.encode('utf8')).hexdigest()

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


def display_spark_results(b):
    global results
    fmd5 = b.tooltip
    j = Javascript(results[fmd5])
    display(j)
