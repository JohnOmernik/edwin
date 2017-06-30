#!/usr/bin/python

import requests
import json
import sys
import random
import os
import os.path
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, line_cell_magic)
from IPython.core.magic import (register_line_magic, register_cell_magic, register_line_cell_magic)


edwin_location = os.path.dirname(__file__)

#####################################################################################################################
@magics_class
class Edwin(Magics):
    myip = None
    matrix = {}
    search_matrix = []
    matrix_core_version = ""
    matrix_org_version = ""
    matrix_user_version = ""
    matrix_replacements = {}
    env_locations = {"edwin_org": "", "edwin_user": ""}

    def __init__(self, shell, *args, **kwargs):
        super(Edwin, self).__init__(shell)
        self.myip = get_ipython()
        for e in env_locations:
            try:
                loc = os.environ[e.upper()]
                env_locations[e] = loc
            except:
                print("%s not provided as %s in ENV: Not Loading" % (e, e.upper()))

        # First Load Core Matrix
        self._load_edwin_matrix(edwin_location + "/edwin.json", "edwin_core")

        # Next load additional matrix components
        for loc in env_locations:
            if env_locations[loc] != "":
                load_dir = env_locations[loc]
                load_matrix = load_dir + "/edwin.json"

                if not os.path.isdir(load_dir):
                    print("Directory %s for %s does not exist - Not Loading!" % (load_dir, loc))
                    break
                if not os.path.exists(load_matrix):
                    print("edwin.json file for %s not found at %s - Not Loading!" % (loc, load_matrix))

                print("%s provided - base location: " % (loc, load_dir))
                sys.path.append(load_dir)
                self._load_edwin_matrix(load_matrix, loc)

        # Cool, let's load up our search matrix and go to town!

        self.search_matrix = self.recurseTree(self.matrix, [], [], True)


        print("Hello, I am Edwin, how may I be of service?")


    def _load_edwin_matrix(self, location, mtype):
        # Open and read file for Matrix Json
        try:
            b = open(location, "r")
            d = b.read()
            b.close()
        except:
            print("Could not read file %s for Edwin %s matrix load" % (location, mtype))
            raise Exception("Edwin %s could not be loaded due to file read issue" % mtype)


        # Load the actual JSON - is it formatted correctly?
        try:
            tmp_matrix = json.loads(d)
        except:
            print("Could not Parse edwin.json %s at %s - Perhaps malformed Json Matrix?" % (location, mtype))
            raise Exception("Non-Parseable JSON Matrix - Json Loads fail")

        # Ok get and set Matrix Version
        try:
            if mtype == "edwin_core":
                self.matrix_core_version = tmp_matrix['matrix_version']
            elif mtype == "edwin_org":
                self.matrix_org_version = tmp_matrix['matrix_version']
            elif mtype == "edwin_user":
                self.matrix_user_version = tmp_matrix['matrix_version']
        except:
            print("Issuing setting Matrix Version - Does your edwin.json have a matrix_version?")
            raise Exception("No matrix_version found")
        # Ok, now get and merge matrix replacements into current replacesments
        try:
            for x in tmp_matrix['replacements']:
                if x in self.matrix_replacements:
                    print("Replacement %s already loaded but will be replaced in Edwin %s" % (x, mtype))
                self.matrix_replacements[x] = tmp_matrix['replacements'][x]
        except:
            print("Issue loading replacements")
            raise Exception("Replacements Exception")

        # Now we look to load edwin_classes from the Matrix
        try:
            loadclasses = tmp_matrix['edwin_classes']
            for cname, mname in loadclasses.items():
                self._load_edwin_subclass(cname, mname)
        except:
            print("No edwin_classes to load in %s - continuing" % mtype)


        #Finally load the matrix tree_root into current matrix
        # we cheat, if this is edwin_core, just assign the tree_root to self.matrix
        if mtype == "edwin_core":
            self.matrix = tmp_matrix['tree_root']
        else:
            # Fine, we need to think through this logic
            # As of now, we will just clobber whole records, so if something exists in a lower level, it will beat up things at a higher level
            for x in tmp_matrix['tree_root']:
                if x in self.matrix:
                    print("Warning!!! %s already exists in the matrix but is being overwritten by %s" % (x, mtype))
                self.matrix[x] = tmp_matrix['tree_root'][x]



    def _load_edwin_subclass(self, class_name, mod_name):

        run_code = "from %s import %s\n" % (mod_name, class_name)
        run_code = run_code + "print(\"Attempting to load %s Magics\")\n" % mod_name
        run_code = run_code + "tclass = None\n"
        run_code = run_code + "ip = get_ipython()\n"
        run_code = run_code + "tclass = %s(ip)\n" % class_name
        run_code = run_code + "ip.register_magics(tclass)\n"
        try:
            self.myip.run_cell(run_code)
        except:
            print("Failed to load Edwin_Class: %s from %s" % (class_name, mod_name))


    # Tree Recursiveness
    def recurseTree(self, nstart, curar, basear, showall):

        for tn in nstart:
            outar = basear + [tn]
            if nstart[tn]['list'] == 1 or showall == True:
                curar.append(outar)
                if 'children' in nstart[tn]:
                    curar = self.recurseTree(nstart[tn]['children'], curar, outar, showall)
        return curar
# Score the input text
    def retScores(self, intext):
        scores = {}
        for x in self.search_matrix:
            tscore = {}
            keywords = x
            score_key = ".".join(keywords)
            cur_score = 0
            found_words = []
            all_match = 1
            for w in keywords:
                if intext.lower().find(w) >= 0:
                    cur_score += 1
                    found_words.append(w)
                else:
                    all_match = 0
                    break
            if all_match == 1:
                # We only include matches where all keywords match. If there are non-matches we ignore
                tscore = {'keywords': keywords, 'found_words': found_words, 'score': cur_score}
                scores[score_key] = tscore
        return scores

# Based on the scores, get the node we need
    def retNode(self, myscores):
        retnode = ""
        if myscores is None:
            retnode = self.matrix["unknown"]
        elif len(myscores) == 0:
            retnode = self.matrix["unknown"]
        elif len(myscores) == 1:
            t = ""
            for x in myscores:
               t = x 
            s = myscores[t]
            retnode = self.getNode(s)
        else:
            leaderar = []
            highscore = 0
            for s in myscores:
                curscore = myscores[s]['score']
                if curscore > highscore:
                    highscore = curscore

            for s in myscores:
                if myscores[s]['score'] == highscore:
                    leaderar.append(s)
            if len(leaderar) == 1:
                retnode = self.getNode(myscores[leaderar[0]])
            else:
                retnode = leaderar
        return retnode

    def getNode(self, score):
        kwar = score['keywords']
        cur = self.matrix
        first = 0
        for x in kwar:
            if first == 1:
                cur = cur['children']
            else:
                first = 1
            cur = cur[x]
        return cur

# We know our resposne node, let's prepare our response based on our Matrix Information!
    def processResp(self, uinput, node):
        if node['type'] == 'rand':
            u = random.choice(node['resp'])
            print(self.replaceText(u))
        elif node['type'] == 'full':
            for u in node['resp']:
                print(self.replaceText(u))
        if 'children' in node:
            if 'cheader' in node:
                child_head = node['cheader']
            else:
                child_head = "This topic also has some related topics you'd be interested in, try referencing:"
            print("")
            print(child_head)
            for x in node['children']:
                desc = "No Desc"
                try:
                    desc = node['children'][x]['short_desc']
                except:
                    pass

                print(" - %s - %s" % (x, desc))
        if 'root' in node:
            print("")
            print("I can offer help on a number of topics, please try mentioning any of these for more details:")
            print("")
            for x in self.matrix:
                desc = "No Desc"
                try:
                    desc = self.matrix[x]['short_desc']
                except:
                    pass
                if self.matrix[x]['list'] == 1:
                    print(" - %s - %s" % (x, desc))

# Replace text in templates
    def replaceText(self, intext):
        outtext = intext
        for x in self.matrix_replacements:
            outtext = outtext.replace(x, self.matrix_replacements[x])
        return outtext



# If we can't determine what was said, processMulti

    def processMulti(self, uinput, rlist):
        print("Mulitple Responses scored to be the same based on your input of %s" % uinput)
        print("I could not guess between the following nodes:")
        for x in rlist:
            print(x)
        print("")
        print("Perhaps more clarity would help me help you... help me help you")
        print("")


    @line_magic
    def edwin(self, line):
        # If nothing is entered, we fix that for the user. We put in Base instead.
        if line == "":
            line = 'edwin'
        myscores = self.retScores(line)
        responseNode = self.retNode(myscores)
        if type(responseNode) is dict:
            self.processResp(line, responseNode)
        else:
            self.processMulti(line, responseNode)

