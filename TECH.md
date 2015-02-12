# Current Technical Items
* Edwin is one file now. This is so we can take Edwin and run it with the run magic and -i flag so all the variables created get created in the global namespace. We should look at organizing the files, while still ensuring easy acces to the iPython main namespace.  This may mean a main edwin.py with some other items that may include org_based data connections, org custom functions, perhaps even setting up files that focus on visualiation etc. I'd like input on best how to do this. 
* We should outline when we try to open connections which failed but not provide ugly errors. For example, if you try to invoke spark but this instance wasn't run with spark setup, it should just outline that in the dataconnection documentation. 
* 

