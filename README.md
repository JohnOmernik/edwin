# edwin
## Enhancing Datascience with iPython Notebooks

Edwin is a framework of helpful scripts you can utilize in data science applications in iPython notebooks. The goal is help keep the flow of data science work in one place. No moving data to a different system to do visualizations, no exporting/importing of datato  move from big data, to small data, to graph data, etc.  

Data science is an investation and data can be anything from images, video, audio, structed, unstructored, code etc.  When we are researching, we want to try to keep information in one place not only to help ourselves as Data Scientists, but to help others who may have to quickly learn or pick up the work later.  

iPython notebooks was choosen due to it's flexibility. There are a number of commercial and even opersource tools on the market desinged to help people do parts of this, however, the idea is to gui-wrap data, that is not goal here, it's part of the result, but not the goal.  The goal here is to make research simple and intuitive. Allowing customization of tools that can produce a repeatable "enviroment" while still allowing easy customization for each users individual enviroment.  

## Design Goals and Vision

* iPython Notebooks was choose due to the iPython's project development goals, including multiuser notebooks and collaborative work. 
* There will be a number of components that are intrisic to Edwin, but also a number of components that going to be unique per enviroment. Our goal will be to find the logical lines so that "How" you interact with your data will be guided by Edwin, but what data you interact will be unique to your enviroment. 
* Precedence will be given to the ease/intuitiveness of the person using Edwin for analytics over the "right way" For example, it may not be right to wrap a call like hashlib.md5('somedata').hexdigest() call into a function like md5() in that it's invoking a new hashlib object every time, however, it is intuitive for a user to just say what's the md5('somedata'). 
* Same goes with modules. We will strive to find a balance in preloading as much as possible without causing issues. That includes numpy, etc when a notebook starts. Why? We don't want a user to be thinking ... hmm I need to do x now, so, wait I have to import something, now declare variables etc. We want there to be something on hand ready to go when the need calls for it. 
* We'd like to create a series of standard widgets.  These widgets should "just work(tm)" in most cases, but if possible allow for further custominzation. 
* Examples:
* * Magic functions where you can run a sql statement and when finished a button appears. That button, when click opens a new window with the results in a nice javascript interactice datagrid.  That way the results ARE stored in the iPython notebook, but wide or tall restults don't interupt the flow of the notebook. 
* 
