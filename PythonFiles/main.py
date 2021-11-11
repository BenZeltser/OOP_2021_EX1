import time
import  numpy
import Names
import csv
import json
import  _json

with open('Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json', 'r') as f:
        jsonObject = json.loads(f.read())
        x = len('elevators')
        for i in range(x+1):
            print("speed of "+str(i)+":")
            print((jsonObject['_elevators'][i]["_speed"]))
            print(jsonObject.get('_speed'))

print(jsonObject)
def setbuildingName(input):
    buildingName = input
    return buildingName


def setoutputName(input):
    outputName = input
    return outputName


def setcallsName(input):
    callsName = input
    return callsName

if __name__ == '__main__':
   ## a = Names.Names(1, 2, 3)
    setbuildingName(input)
    setcallsName(input)
    setoutputName(input)
