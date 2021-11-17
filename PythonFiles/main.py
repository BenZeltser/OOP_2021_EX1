import time
import numpy
import Names
import csv
import json
import _json
import threading
import time

'''
***JSON***

with open('Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json', 'r') as f:
    jsonObject = json.loads(f.read())
    x = len('elevators')
    for i in range(x+1):
        print("speed of "+str(i)+":")
        print((jsonObject['_elevators'][i]["_minFloor"]))
        print(jsonObject.get('_speed'))

'''
'''
    ***TODO**
    1.Get files and info (JSON and CSV)
    2.Create Building instance and insert info from files
    3.Insert Elevator list to Building
    4.Iterate Through the CALLS and place them
    5.Export CSV file according to the JAVA program
'''


class main():

    #bName=input("enter building number")
    #fileName="B"+bName+".json"
    with open('b5.json','r') as fileOne:
        building=json.load(fileOne)
    Cname=input("enter call type (choose a letter from a to d)")
    filename2="Calls_"+"d.csv"
    #with open(filename2,'r') as FileTwo


    global buildingName
    global outputName
    global callsName

    def __init__(self,buildingName,outputName,callsName):
        self.buildingName=buildingName
        self.outputName = outputName
        self.callsName = callsName

    '''
        Code Owners: 313327579, 2088...
    '''
    global ID0,ID1
    ID0=313327579
    ID1 =208849620

    elevetorCalls=[]


if __name__ == '__main__':
    pass


