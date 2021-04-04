import numpy as np
import csv
import plotly.express as px

with open("Coffee.csv") as q:
    r = csv.DictReader(q)
    fig = px.scatter(r,x = "hours", y = "Coffee")
    fig.show()

def getdatasrc(path):
    Coffee = []
    hours = []
    with open(path) as file:
        df = csv.DictReader(file)
        for row in df:
            Coffee.append(float(row["hours"]))
            hours.append(float(row["Coffee"]))
    return{
        'x':hours,
        'y':Coffee
    }

def findcorrelation(Data):
    correlation = np.corrcoef(Data['x'],Data['y'])
    print(correlation)

def main():
    Datapath = '/Users/mac/Desktop/Xcode_python/Otherprograms/Coffee.csv'
    datasrc = getdatasrc(Datapath)
    findcorrelation(datasrc)

main()

