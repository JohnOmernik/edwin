# Design Goals and Vision for the Edwin Project

* iPython Notebooks was choose due to the iPython's project development goals, including multiuser notebooks and collaborative work. 
* There will be a number of components that are intrisic to Edwin, but also a number of components that going to be unique per enviroment. Our goal will be to find the logical lines so that "How" you interact with your data will be guided by Edwin, but what data you interact will be unique to your enviroment. 
* Precedence will be given to the ease/intuitiveness of the person using Edwin for analytics over the "right way" For example, it may not be right to wrap a call like hashlib.md5('somedata').hexdigest() call into a function like md5() in that it's invoking a new hashlib object every time, however, it is intuitive for a user to just say what's the md5('somedata'). 
* Same goes with modules. We will strive to find a balance in preloading as much as possible without causing issues. That includes numpy, etc when a notebook starts. Why? We don't want a user to be thinking ... hmm I need to do x now, so, wait I have to import something, now declare variables etc. We want there to be something on hand ready to go when the need calls for it. 
* We'd like to create a series of standard widgets.  These widgets should "just work(tm)" in most cases, but if possible allow for further custominzation. 
* Help should be intuitive and built in. I.e. We should have a series of magics that help a user do what they are trying to do.  %edwin will be the initial helper magic. Let's try to make others helpful and intuitive. 
# Examples:
* Magic functions where you can run a sql statement and when finished a button appears. That button, when click opens a new window with the results in a nice javascript interactice datagrid.  That way the results ARE stored in the iPython notebook, but wide or tall restults don't interupt the flow of the notebook. 
* Graphing/Visualiation should be a magic as possible. Yes we will want to tweak, but given a set of data, we should be able to "try" to make a certain graph and if it doesn't work, still accept modifications.
* 


