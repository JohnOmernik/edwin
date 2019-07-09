# edwin
Enhancing Datascience With IPython Notebokes
-----
FAQ: 

Q: But it's call Jupyter now, why is IPython still in the name? A: Because Edwjn doesn't make sense. 

----


By working with a distributed implementation of Jupyter Notebooks, especially on an architecture that supports spawning of notebook servers on demand such as JuypyterHub using Mesos and Marathon (https://github.com/JohnOmernik/marathonspawner)
We have a platform for knowledge transfer using data, rather than a platform just to analyze data.  This platform is extensible, meaning organizations  (and users!) can come up with their own modules (although share back is welcome!).  This is MVP of 
the concept, but even in it's MVP form, I am finding value in using it everyday. I am hoping to continue building this going forward. 

## Installing Edwin
- Edwin should be installed on your JupyterNotebook server. If you have a single Jupyter Notebook server, install it there, otherwise, install it in containers that will run your server. 
    - python setup.py install 
- Edwin has some basic requirements - Additional custom classes may have their own requirements. Any classes moved into Edwin Core that have additional requirements will update this list. 
    - requests
    - numpy
    - pandas
    - IPython
    - mpld3
    - matplotlib
-

## Design of Edwin
Edwin is simple, it's a class that defines edwin, and an edwin.json.  The idea is that edwin.json that ships with this repo should remain unmodified. It's the "Core" personality. 
Obviously, we will update the personality, and add other classes that are deamed important to the core functions, but for now, this should remain as is.  

The next "Layer" of Edwin is "Edwin Org"

This is where you can setup a directory in a shared location with customized json and classes for your organization.  To have the edwin_core load your edwin_org, just start your notebook server with a ENV variable: EDWIN_ORG which is a path 
to the location with the edwin.json in it.  This can be a location directory synced (harder) or it can be a shared location like a NFS drive (easier). This is where you can put in customizations for your org, data definitions, custom classes 
for accessing data, etc.  There is a an example edwin_org at https://github.com/johnomernik/edwin_org  This repo has a class for Apache Spark, Apache Drill and a demo class to build others off of.  I would love to see community around there where 
classes can be built at the org level, and then be shared with the community and even voted into edwin core for upkeep purposes. 

The next "Layer" of Edwin is "Edwin User"

This is where users of notebooks can come up with their own reminders, and pieces of Edwins Personality. In addition they can build their own classes that they use to help with their data anlysis.  If they do this, and prove value they can easily
move their class from edwin_user to edwin_org and then have it shared with their organization. To set a location for edwin_user, put a path to in the ENV variable EDWIN_USER in the root of that path, have a edwin.json. 


## Import ENV Variables
When starting a notebook server, there are ENV variables that are important to the operation of Edwin - Note there are other variables that Edwin may use for "replacements" That's a feature where you can code in the json variables
so that user specifc things passed in from the ENV are replaced in Edwin's responses. 

| Variable             | Req/Opt | Desc |
| --------             | ------- | ---- |
| EDWIN_ORG            | OPT     | This is the path the Edwin Org, while Optional, it's highly recommended |
| EDWIN_USER           | OPT     | The path to Edwin User.  Optional and not required |
| JUPYTERHUB_USER      | OPT     | This is the user running in the notebook. Edwin uses this to replace "%nbuser% in responses. So if you set this on your notebook server, it helps Edwin customize things|


## edwin.json
Format/Desc of edwin.json will be coming shortly. 

# Ideas Planned
- Feedback. Have users be able to send feedback on stuff they want to see in Edwin
- Reminders - Have users be able to ask edwin to do something based on some keywords. (This is like auto updating the edwin_user and perhaps edwin_org without having to manually update the json)
- Backends for edwin.json? Since we just use structured json, we could perhaps see some advantage with a document store in the future
- More visualizations/examples
- Interface to allow for searching notebooks based on an Elastic Serarch back end. Be able to ask Edwin to search for you
- More to come!

