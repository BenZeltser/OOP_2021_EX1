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
    B5 = json.load(f)

print(B5.items())
#Convert JSON content to a string / DICT

idList = []

# HOW TO ACCESS A FILE: --> JsonFile['_elevators][index][attribute]

#EXAMPLE FOR ELEVATOR 1

for elevator in B5['_elevators']:
    print(elevator['_id'])
    print()
    _id = B5['_elevators'][1]['_id']
    _speed = B5['_elevators'][1]['_speed']
    _minFloor = B5['_elevators'][1]['_minFloor']
    _maxFloor = B5['_elevators'][1]['_maxFloor']
    _closeTime = B5['_elevators'][1]['_closeTime']
    _openTime = B5['_elevators'][1]['_openTime']
    _startTime = B5['_elevators'][1]['_startTime']
    _stopTime = B5['_elevators'][1]['_stopTime']
#Run example

e1 = Elevator.Elevator(_id,_speed,_minFloor,_maxFloor,_closeTime,_openTime,_startTime,_stopTime)

#INSTANCE COMPLETE



'''
    *   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   *
    CSV 
    *   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   **   *   *   *
'''


with open ('Calls_d.csv', 'r') as f:
    calls_d = csv.reader(f)
    for line in calls_d:
        pass
