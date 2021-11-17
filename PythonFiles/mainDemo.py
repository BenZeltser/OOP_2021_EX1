import Elevator
import csv
import _csv
import json
import _json

class mainDemo():
    pass

'''
    JSON
'''
#Open the file and read from it
with open ('B5.json', 'r') as f:
    jsonFile = json.load(f)

print(jsonFile.items())
#Convert JSON content to a string / DICT

idList = []

# HOW TO ACCESS A FILE: --> JsonFile['_elevators][index][attribute]

#EXAMPLE FOR ELEVATOR 1

for elevator in jsonFile['_elevators']:
    print(elevator['_id'])

_id = jsonFile['_elevators'][1]['_id']
_speed = jsonFile['_elevators'][1]['_speed']
_minFloor = jsonFile['_elevators'][1]['_minFloor']
_maxFloor = jsonFile['_elevators'][1]['_maxFloor']
_closeTime = jsonFile['_elevators'][1]['_closeTime']
_openTime = jsonFile['_elevators'][1]['_openTime']
_startTime = jsonFile['_elevators'][1]['_startTime']
_stopTime = jsonFile['_elevators'][1]['_stopTime']
#Run example

e1 = Elevator.Elevator(_id,_speed,_minFloor,_maxFloor,_closeTime,_openTime,_startTime,_stopTime)

#INSTANCE COMPLETE