import pandas as pd
from test import testname 
import os.path

def exportCSV(dfPanda, name, sorted):
    if sorted:
        if name.endswith(".csv"):
            name = name.replace(".cvs","")
        name = name+'_sorted'
    else:
        if name.endswith(".csv"):
            name = name.replace(".cvs","")
        name = name+'_unsorted'
    if not name.endswith(".csv"):
        name = name+ '.csv'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_csv(path)


def exportJSON(dfPanda, name,sorted):
    if sorted:
        if name.endswith(".json"):
            name = name.replace(".json","")
        name = name+'_sorted'
    else:
        if name.endswith(".json"):
            name = name.replace(".json","")
        name = name+'_unsorted'
    if not name.endswith(".json"):
        name = name+ '.json'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_json(path)


def exportPICKLE(dfPanda, name,sorted):
    if sorted:
        if name.endswith(".pl"):
            name = name.replace(".pkl","")
        name = name+'_sorted'
    else:
        if name.endswith(".pkl"):
            name = name.replace(".pkl","")
        name = name+'_unsorted'
    if not name.endswith(".pkl"):
        name = name+ '.pkl'
    path = os.path.join(__file__.replace("exportSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    print(path)
    dfPanda.to_pickle(path)
