import time
import csv
import _json
import threading
import time
import json
import ElevatorAlgo
import ElevatorCall
import Elevator
import Building

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
    2.Create buildingClass instance and insert info from files
    3.Insert Elevator list to buildingClass
    4.Iterate Through the CALLS and place them
    5.Export CSV file according to the JAVA program
'''


class main():
    global ID0, ID1
    ###############
    ID0 = 313327579
    ID1 = 208849620
    ###############

    '''
        t1.) Get Json data
    '''
    bName = input("enter building number")
    fileOne = "B" + bName + ".json"
    with open(fileOne, 'r') as fileOne:
        buildingFile = json.loads(fileOne.read())

    '''
        t2.) get CSV Data and output the out.csv file
    '''

    Cname = input("enter call type (choose a letter from a to d)")
    filename2 = "Calls_" + Cname + ".csv"
    with open(filename2, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        '''
            Allocate Elevators to 'allCalls'
        '''
        # Set the writing

        with open('pelet.csv', 'w', newline='') as f:
            fieldnames = ['Elevator call', 'time', 'SRC', 'DST', 'Status', 'Elevator allocated']
            theWriter = csv.DictWriter(f, fieldnames=fieldnames)

            # Write to the file

            amaxfloor = buildingFile['_minFloor']
            aminfloor = buildingFile['_maxFloor']
            elevators = buildingFile['_elevators']

            # Create instance for each elevator - not sure if needed

            elevatorsList = []
            for i in range(len(elevators) - 1):
                anElevator = Elevator.Elevator(
                    elevators[i]['_id'],
                    elevators[i]['_speed'],
                    elevators[i]['_minFloor'],
                    elevators[i]['_maxFloor'],
                    elevators[i]['_closeTime'],
                    elevators[i]['_openTime'],
                    elevators[i]['_startTime'],
                    elevators[i]['_stopTime'])

                elevatorsList.append(anElevator)
            abuilding = Building.building(aminfloor, amaxfloor, elevatorsList)
            algo = ElevatorAlgo.elevatorAlgo(abuilding)

            theWriter.writeheader()

            for call in csv_reader:
                # Activate the Allocation algorithm

                '''
                    *****PLACE CODE HERE*****

                    Description:
                        1.Create allCalls[]
                        2.Allocate an Elevator for the call
                        3.Change the value of of call[5] to the index of the allocated Elevator
                        HENCE: call[5] = Algo.Allocate

                '''
                currentcall = ElevatorCall.CallForElevator(call[0], call[1], call[2], call[3])
                indexElevator = algo.allocateAnElevator(currentcall,abuilding)
                call[5] = indexElevator
                theWriter.writerow({'Elevator call': call[0],  # always the same
                                    'time': call[1],
                                    'SRC': call[2],
                                    'DST': call[3],
                                    'Status': call[4],  # always 0
                                    'Elevator allocated': call[5]})




