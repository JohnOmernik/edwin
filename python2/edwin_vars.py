# These are the variables specific to Edwin


# Change how Edwin refers to you. 
greeting = "Sir" # Could be, Maam, could be hey you, we should write a function to change it :) 


#This may not be needed if Edwin is autolaoded
# edwin's location
#edwin_loc = os.path.dirname(os.path.realpath(__file__))

# This is where the results are stored for the magics, this may get large, we should probably keep tabs on that. 
results = {}

# For the magics, it's one thing to just display, but after you run a magic query, it would be nice if you were like "Oh damn, I want those results" well you can with the prev_spark, and other "prev" variables.  We should create one for each magic. 
prev_file = ""
# Define out your custom data sources here
# The actual definition section is  moved to the  "custom" area for each org.  WE should also add a dictionary item that indicates if the Data Src instantiation was successful
datasrcs = []


#example datasrc:

#datasrc = {}
#datasrc['name'] = "Spark Context"
#datasrc['desc'] = "Default Connection to local Spark Context"
#datasrc['var'] = 'sc'
#datasrc['code'] = 'pass'
#datasrc['instantiated'] = False
