import time
import numpy
import Names
import csv
import _json
import threading
import time
import json
import ElevatorAlgo
import ElevatorCall
import Elevator

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

    global ID0,ID1
    ###############
    ID0=313327579
    ID1=208849620
    ###############
    '''
       t1.) Get 3 Strings
    '''
    bName=input("enter building number")
    fileOne= "B" + bName + ".json"
    with open('B5.json','r') as fileOne:
        building=json.load(fileOne)

    Cname=input("enter call type (choose a letter from a to d)")
    filename2= "Calls_" + "d.csv"
    with open(filename2,'r') as FileTwo:
        csv = csv.reader(FileTwo)

    allCalls=[]
    for i in range(len(elevetorCalls)):
        thisCall=elevetorCalls[i]
        elev=ElevatorAlgo.allocateAnElevator(thisCall)
        thisCall.setElevator(elev)






if __name__ == '__main__':
    pass




'''
    t2.) get Json files
'''











'''
    t3.) get CSV files
'''










'''
    t4.) output CSV file
'''

    #Set the writing

with open('KUKURIKU440.csv', 'w', newline='') as f:
    fieldnames = ['Elevator call','time','SRC','DST','Status','Allocated to (index)']
    theWriter = csv.DictWriter(f, fieldnames=fieldnames)

    #Actually start writing

    theWriter.writeheader()

    #insert each info accordingly

    for row in calls:
        theWriter.writerow({'Elevator call':1, #always the same
                            'time':2,
                            'SRC':3,
                            'DST':4,
                            'Status':5,         #always -1
                            'Allocated to':6})