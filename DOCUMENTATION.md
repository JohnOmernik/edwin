# How to use Edwin
Edwin is designed for easy integration with iPython. The goal is to be one system that is both standarized for easy sharing of ideas while still customizaable so that each enviroment has a tailored Edwin. 

* Edwin works great with iPython as the Python Shell for Spark. We hope to flush out more use cases for Edwin with Spark going forward. Including helper functions for graphx, mllib, spark streaming. 

* You can run Edwin without Spark.  We should detect this on execution so we do get errors if we try to invoke spark variables and they fail

* Edwin will require certain packages like numpy and matplotlib.  Install those on your server.  We should discuss making them optional, or required, the goal here is a standardized enviroment. 

* To run edwin make the first line of your notebook (or set the execute on open config option, ensure name space)
% run /path/to/edwin.py -i 


## Example of running Edwin with iPython Notebooks and a Spark Shell on Mesos
IPYTHON_OPTS="notebook --matplotlib inline --ip=%LISTENIP% --no-browser --port=%LISTENPORT%" %PATHTOSPARKHOME%/bin/pyspark --master mesos://%MESOSMASTER%:5050 --driver-memory 1G --executor-memory 4096M

%LISTENIP% = The IP address you want to run the webserver for iPython Notebooks
%LISTENPORT% = The Port you are listening on for iPython Notebooks
%PATHTOSPARKHOME% = The Spark home, for example /opt/mapr/spark/spark-1.2.0-bin-mapr4 
%MESOSMASTER% = The Master for your Mesos Cluster

Obviously you can updated the Driver Memory and the Executor memory as needed. 


