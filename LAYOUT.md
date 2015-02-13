#Shell Layout for Edwin
Each developed shell should contain a number of files. Here is an example of the files and descriptions as stored in the python2 shell  

## edwin_imports.py and edwin_imports_custom.py
edwin_imports.py contains multiple import functions to ensure certain modules are preloaded when edwin loads. edwin_imports_custom.py are the imports that are specific to my enviroment (i.e. hive and spark) You could also add others here. 

## edwin_vars.py and edwin_vars_custom.py
These are the global variables that are defined for the user. The custom file is obviously those specifc to the enviroment. The non-custom one has a a deictionary of datasrcs that can be filled in in the _custom file. 

## edwin_funcs.py and edwin_funcs_custom.py
These are functions that are available to the user _custom are the functions specific to your enviroment.  These functions include non-magic functions that simplify things. An example of this is md5() which basically wraps hashlib.md5(data).hexdigest()

##edwin_magics.py and edwin_magics_custom.py
These are magic functions designed to be intuitive to the user. These are items where it doesn't make sense to use a function like when we want to run a SQL statement instead of double quote encasing it, just use magic!

## edwin.py  
This is just a printed greeting. Not sure how to use this, as the startup folder in an iPython profile doesn't print anything. This may be removed in the future. 
