import pandas as pd
import os.path


def importCSV(name):
    if not name.endswith(".csv"):
        name = name + '.csv'
    path = os.path.join(__file__.replace("importSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    df = pd.read_csv(path, usecols=range(1,6))
    return df

def importJSON(name):
    if not name.endswith(".json"):
        name = name + '.json'
    path = os.path.join(__file__.replace("importSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    df = pd.read_json(path)
    return df

def importPICKLE(name):
    if not name.endswith(".pkl"):
        name = name + '.pkl'
    path = os.path.join(__file__.replace("importSAVE.py",""), "YOUR_DATA")
    path = os.path.join(path, name)
    df = pd.read_pickle(path)
    return df
