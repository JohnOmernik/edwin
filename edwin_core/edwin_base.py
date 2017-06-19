#!/user/bin/python

#Core IPython Imports
#from IPython.core.magic import (register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
from nbformat import v4 as nbf
from nbformat import write as nbfwrite
from IPython.core.display import HTML
from IPython.display import display_html, display, Javascript, FileLink, FileLinks, Image
import ipywidgets  # Widget definitions

# Python Imports
import hashlib
import os
import os.path
import sys
import requests
import re
import json
import random
# Third Party Import IPython Imports - Need to install
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import mpld3

# Plots to be inline
#try:
#    get_ipython().enable_matplotlib('inline')
#except:
#    print("##################")
#    print("matplotlib inline failed, probably not in a notebook are you?")
#    print("Don't worry, we'll go on")
#    print("##################\n")

edwin_location = os.path.dirname(__file__)


#####################################################################################################################
@magics_class
class Edwin(Magics):
    matrix_version = ""
    matrix_data = {}
    edwinmagics = {}
    datasrcs = {}
    functions = {}
    env_locations = {}
 #    datasrc record
 #    {"name": "gisprodrill", "desc":"Gis Prod Apache Drill", "var": "gisproddrill", "magic": "drill", "instantiated": False, prevresults: []}


    def __init__(self, shell, *args, **kwargs):
        super(Edwin, self).__init__(shell)
        self._load_edwin_core_matrix()

        env_configs = { "edwin_org_data": False, "edwin_org_code": False, "edwin_user_data": False, "edwin_user_code": False }
        for e in env_configs:
            try:
                l = os.environ[e.upper()]
                tmp = {"file_path": l, "loaded":False}
                self.env_locations[e] = tmp
                if e.find("code") >= 0:
                    self._load_edwin_code(e)
            except:
                if env_configs[e] == True:
                    raise Exception("%s is required to be passed in env variables, but not found" %  e.upper())

        print("Hello, I am Edwin, how may I be of service?")

       # for m in env_locations:
#            res = self._load_edwin_matrix(m)
#            if m != 0:
#                print("Unable to load %s" % s)

    def _load_edwin_code(self, loc):
        if os.path.isfile(self.env_locations[loc]['file_path']):
            print("%s exists!" % self.env_locations[loc]['file_path'])
            self.env_locations['loc']['loaded'] = True
        else:
            print("Can't find: %s" % self.env_locations[loc]['file_path']))


    def _load_edwin_matrix(self, matrix):
        retval = 0
        try:
            b = open(matrix, "r")
            d = b.read()
            b.close()
            cur_matrix = json.loads(d)

        except:
            print("Could not open %s" % matrix)
            retval = 1
        return retval

    @line_magic
    def edwin(self, line):
        self.ask(line)

        return line

    @line_magic
    def matrix(self, line):
        print(self.pprintJSON(self.matrix_data))
        print(self.pprintJSON(self.env_locations))
        return line

    def _merge_matrix(self, newmatrix):
        print("I need to merge me some matrix")

    def pprintJSON(self, indata):
        return json.dumps(indata, sort_keys=True, indent=4, separators=(',', ': '))

    def _load_edwin_core_matrix(self):
        try:
            b = open(edwin_location + "/edwin.json", "r")
            d = b.read()
            b.close()
            self.matrix_data = json.loads(d)
            self.matrix_vers = self.matrix_data['version']
            print("Edwin Matrix Version %s Loaded and ready" % self.matrix_vers)
        except:
            print("I could not find my core self - It's time for me to on a journey to find me")
            raise Exception("Edwin Core Matrix edwin.json not found")


    def ask(self, intext):
        print('In "Ask"')
        # This is what gets called first from here we
        # 1. Parse the text into locations based on our core matrix
        # 2. Once we've identified the core location, we get a response
        # 3. We pass the text to a formater function
        # 4. We deplay the formatted response. 
        print(self.formatResponse("You asked me: %s" % intext))

    def parseInput(self, intext):
        return intxt
        # Determine where we should go
        # return a tree location
        # We need to figure out context as an interative thing... perhaps weights?


    # Return a random response from the list of responses
    def getResponse(self, resp, respdata):
        if resp not in self.matrix_data:
            resp = "UNKNONWN"
        return random.choice(self.matrix_data['responses'][resp])

    def formatResponse(self, resp):
        return resp


def main():
    print("This is for testing puposes")
    e = Edwin()







if __name__ == "__main__":
    main()
