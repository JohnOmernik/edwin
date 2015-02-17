# Installation of all thing Edwin

This is a from scratch installation of Edwin. I included some information on my setup, incluing paths to help explain some of the challenges or underlying archeticture.  

## Server
* Ubuntu 14.04 Running on VMWare
* 8 GB of ram with 2 Assigned Cores
* 45 GB of hard drive space
* Standard Install, no LVM, only package I added was open SSH

## Main Components
* Jupyter (iPython 3)
* Jupyter Hub

## Additional things for my enviroment
* MapR Client for MapR Hadoop
* pyhs2 For Connection to HiveServer2
* Mesos 
* Mapr Spark 1.2 


## First steps
* Install Ubuntu 14.04
* Setup initial users 
* Setup Network IPs/DNS etc
* sudo apt-get update 

Alwas good to keep things up to date
* sudo apt-get upgrade

Stuff for my enviroment (Needed to add MapR Packages)
* sudo apt-get install mapr-client nfs-client

MapR puts everything in /opt/mapr.  For me, I find that a nice place to put things.  Here are the paths I am using on my edwin server for example:

/opt/mapr/mesos - Root of all things mesos
/opt/mapr/spark - Root of all things spark
/opt/mapr/edwin - Root of all thigns edwin
/opt/mapr/edwin/edwin - The clone of the edwin git. (I ran git clone from /opt/mapr/edwin/
/opt/mapr/edwin/edwin_custom - The location for the customer edwin files for my enviroment.  
/opt/notebooks - Root location for all my notebooks on my shared server

## Spark and Mesos
Since I am running a Mesos Cluster and Spark, I needed to install some things:
* mesos-0.21.0.tar.gz  (from Apache.org)
* spark-1.2.0-bin-mapr4.tgz (Either from MapR or Apache)
To help things along, install these
* sudo apt-get install build-essential python-dev python3-dev make gcc 

### Mesos
These commands from:
http://mesos.apache.org/gettingstarted/
Using Open JDK7
sudo apt-get install openjdk-7-jdk
sudo apt-get install python-dev python-boto
sudo apt-get install libcurl4-nss-dev
sudo apt-get install libsasl2-dev
sudo apt-get install maven
sudo apt-get install libapr1-dev
sudo apt-get install libsvn-dev

All on one line (I removed python-dev because I already got it in the previous step)
sudo apt-get install openjdk-7-jdk python-boto libcurl4-nss-dev libsasl2-dev maven libapr1-dev libsvn-dev

In my Mesos directory:

mkdir build
cd build
../configure
make

sudo make install
## Initial Tests

At this point, I copied my spark config files from original server, and all seemed well, my /etc/hosts did have my hostname (edwin) pointing to 127.0.1.1 which messed things up, when I removed that, the pyspark shell worked great as did hive integration. 

### Spark

This is even easier, I untared the spark bin tgz into /opt/mapr/spark.  I copied my conf over for my cluster and it worked

# Next iPython Notebooks!

Remeber from above, I use /opt/mapr for all my "installed" programs and /opt/notebooks as my notebook root. 

## Installing iPython3/Jupyter.
Ubuntu 14.04 comes with Python 3.4 installed so I just added setuptools and pip for both python2 and python3

- sudo apt-get install python-setuptools python3-setuptools python-pip python3-pip
Then I install iPython:
- sudo pip install --pre "ipython[all]"
- sudo pip3 install --pre "ipython[all]"


##Install the iPython2 Kernel
This is important so you have the python2 kernel available in Jupyter
- sudo ipython2 kernelspec install-self

## Jupyter Hub
Jupyter hub is what is evolving to use the multiuser setups we all desire. This is beta, however, I am just running with it as eventually we need to have it in place, and would prefer to have it runnin



- sudo mkdir /opt/mapr/jupyter
- csudo hown user:user /opt/mapr/jupyter
- cd /opt/mapr/jupyter
- sudo apt-get install git
- sudo apt-get install npm nodejs-legacy
- sudo npm install -g bower less jupyter/configurable-http-proxy
- git clone https://github.com/jupyter/jupyterhub.git
- cd jupyterhub
- pip install -r requirements.txt
- pip3 install -r requirements.txt
- python3 setup.py install

At this point JupyterHub is installed. I have a Jupyterhub config file in /opt/mapr/jupyter and I run jupyterhub (Right now as root, in teh future with sudo spawner and a non-priv user) by executing screen, then going to /opt/mapr/jupyter and running sudo jupyterhub


# Edwin
This is the core of our modules.  

- mkdir /opt/mapr/edwin
- cd edwin
- git clone https://github.com/WalterDalton/edwin.git
## Get Edwin Modules
These modules are what is required by edwins core to run. 
(The following is require for matplotlib)
- sudo apt-get install libfreetype6-dev libxft-dev

Note: I install all modules for python2 and python3.  It just feels right. 
- sudo pip install matplotlib 
- sudo pip3 install matplotlib
- sudo pip install pyhs2
- numpy was already installed by matplotlib
- sudo pip install pandas
- sudo pip3 install pandas
- sudo pip install mpld3
- sudo pip3 install mpld3
- sudo pip install networkx
- sudo pip3 install networkx
