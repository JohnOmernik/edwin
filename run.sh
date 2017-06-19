#!/bin/bash

# This is a shell script to run a docker container with /app mount to pwd. This is designed to facilate testing of Edwin

IMG="dockerregv2-shared.marathon.slave.mesos:5005/jupyternotebook:0.7.2"


sudo docker run -it --rm -v=`pwd`:/app $IMG /bin/bash


