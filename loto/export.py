import pandas as pd
from test import testname 

def exportCSV(dfPanda, name):
    dfPanda.to_csv(name, index = False)