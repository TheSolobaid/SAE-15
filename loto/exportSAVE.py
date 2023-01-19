import pandas as pd
from test import testname 
import os.path

def exportCSV(dfPanda, name, sorted):
    if sorted:
        name = name+'_sorted'
    else:
        name = name+'_unsorted'
    if not name.endswith(".csv"):
        name = name+ '.csv'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_csv(path)


def exportJSON(dfPanda, name,sorted):
    if sorted:
        name = name+'_sorted'
    else:
        name = name+'_unsorted'
    if not name.endswith(".json"):
        name = name+ '.json'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_json(path)


def exportPICKLE(dfPanda, name,sorted):
    if sorted:
        name = name+'_sorted'
    else:
        name = name+'_unsorted'
    if not name.endswith(".pkl"):
        name = name+ '.pkl'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_pickle(path)
