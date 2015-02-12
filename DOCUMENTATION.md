# How to use Edwin
Edwin is designed for easy integration with iPython. The goal is to be one system that is both standarized for easy sharing of ideas while still customizaable so that each enviroment has a tailored Edwin. 

## Global Prerequisites
All Edwin development will be based on iPython 3+ (currently in Dev as of 2015-02-15). This means there are certain requirements that you must install. We recommend also installing JupyterHub for best future stability. 

- iPython 3 (and all requirements)
- Python 3.4+ *
- Jupyterhub (This is sorta optional, but just install it and do it this way from the start... please?)

* While Python3 is a requirement, the code in Edwin uses an iPython2 Shell, we will probabably develop a system of tools that will customize an Edwipin per the shells you are using. If you want Edwin in a new shell, we recommend looking at the setup we did for Python2 and creating an Edwin for a new shell... please upload if you get-it-done!

## Edwin - Python2 Shell 
### Requirements
- matplotlib
- numpy
- mpld3
- pandas

### Optional
- pymongo
- pyhs2
- Spark

### Python2 Installation
- Install Python2 shell in iPython3 (example... )
- Git edwin
- Determine where the files will be located. This should be in a location that all users who will be using edwin have access to
- For each user
 - Create the default profile: ipython profile create
 - run ./install_edwin.sh /path/to/edwin/python2 default
 - This run command will have be run for each user who will use edwin. This create links in the startup folder of the ipython default profile for the user and allows you to keep one running instance of edwin going. 






