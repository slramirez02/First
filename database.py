print("This is the database.py file")
print("Python thinks this is named {}".format(__name__))

import blood_calculator as bc
from blood_calculator import HDL_analysis 

#all functions within BC without blood_calculator 
#can cause conflicts with matching function names (run, stop, plot, etc.)
#better to leave leave trail of function origins
from blood_calculator import * 

HDL_value = 25
analysis = HDL_analysis(HDL_value)
print("The result is {}".format(analysis))