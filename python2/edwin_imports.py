#Core IPython Imports

from IPython.core.magic import (register_line_magic, register_cell_magic, register_line_cell_magic)
from IPython.nbformat import v4 as nbf
from IPython.nbformat import write as nbfwrite
from IPython.core.display import HTML
from IPython.display import display_html, display, Javascript, FileLink, FileLinks, Image
from IPython.html import widgets # Widget definitions

# Python Imports
import hashlib
import os
import sys
import re
# Third Party Import IPython Imports - Need to install
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import pandas as pd

#Set plots to be inline
get_ipython().enable_matplotlib('inline')
