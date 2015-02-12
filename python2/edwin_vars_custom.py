# Custom Data Source Definition


datasrc = {}
datasrc['name'] = "Spark Context"
datasrc['desc'] = "Default Connection to local Spark Context"
datasrc['var'] = 'sc'
datasrc['code'] = 'pass'
datasrc['instantiated'] = False
datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Spark Hive Context"
datasrc['desc'] = "Connection to Spark Cluster Hive Context"
datasrc['var'] = 'sparkhc'
datasrc['code'] = 'sparkhc = HiveContext(sc)'
datasrc['instantiated'] = False

datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Spark SQL Context"
datasrc['desc'] = "Connection to Spark Cluster SQL Context"
datasrc['var'] = 'sparksql'
datasrc['code'] = 'sparksql = SQLContext(sc)'
datasrc['instantiated'] = False

datasrcs.append(datasrc)

datasrc = {}
datasrc['name'] = "Hive"
datasrc['desc'] = "Connection to Hive Server2 on Alphaking"
datasrc['var'] = 'hive'
datasrc['code'] = "hive = pyhs2.connect(host='alphaking',port=10000,authMechanism='PLAIN',user='darkness',password='removed',database='default')"
datasrc['instantiated'] = False

datasrcs.append(datasrc)


# This actual runs all the datasrcs. It should try them and then set a variable in the datasrc if the instantiation was successul. 
for src in datasrcs:
    try:
        exec src['code']
        src['instantiated'] = True
    except:
        pass
