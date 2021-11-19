import math
import Building
from ElevatorCall import CallForElevator



class elevatorAlgo:

    global ERROR, DOWN, LEVEL, UP,GOING2SRC, GOING2DST, DONE
    ERROR= -2
    DOWN = -1
    LEVEL = 0
    UP = 1
    GOING2SRC=1
    GOING2DST=2
    DONE=3

    def __init__(self, building: object):
        self.building = building

#returns the building the algorithm is currently working on
    def getBuilding(self):
        return self.building

#returns the name of the algorithm
    def algoName(self):
        return "EX1_OOP_Smart_Elevator_Algo_Offline"

#calculate the distance between an elevator and a destantion
    def distance(self,elevatorIndex, src):
        answer=-1
        elev= Building.getElevator(elevatorIndex)
        pos=elev.getPos()
        speed=elev.getSpeed()
        startNstop=elev.getStartTime()+elev.getStopTime()
        stopTime=elev.getStopTime()
        state=elev.getState()
        distance=math.fabs((src-pos))
        if src==pos:
            return 0
        if state==LEVEL:
            answer=distance*speed+startNstop
        elif state==UP or state==-DOWN:
            answer=distance*speed+stopTime
        return answer

#this function returns if an elevator can be assigned to a call
    def isValid(self,direction,floorCall,pos,elevDirection):
        if elevDirection!=0:
            if elevDirection!=direction:
                return False
        if direction==UP:
            if pos>floorCall:
                return False
        elif direction==DOWN:
                if pos<floorCall:
                    return False
        return True

#returns if the elevator is a downcalls elevator or upcalls elevator
    def upOrDown(self,ele):
        return ele.getCallType()

#returns the distanced (in floors) between an elevator destantion and and source of the call
    def abDST(self,myPos,DST):
        return math.fabs((myPos-DST))
        
    
#this is the main algorithm, it checks between all the elevators and returns the closest elevator to the source
    def allocateAnElevator(self,callForElev: CallForElevator):
        index=-1
        elevatorIndex=0
        src=callForElev.getSrc()
        distance=-1
        building = Building.building(-10,100)
        elevators = building.elevators
        for elevator in elevators:
            print("CONTENT")
            print(elevator.get_dest())
            while elevator!=None:
                if elevator.getState()==ERROR:
                    elevatorIndex+=1
                    continue
                pos=elevator.getPos()
                if self.isValid(elevator.getState(),src,elevator.getCallType())==True:
                    tempDist=self.distance(index,src)
                    if tempDist!=-1:
                            if tempDist==0:
                                return elevatorIndex
                            elif distance==-1:
                                    distance=tempDist
                                    index=elevatorIndex
                            elif tempDist<distance:
                                    distance=tempDist
                                    index=elevatorIndex
                    elevatorIndex+=1
                    elevator=Building.Building.getElevator()
                    if index==-1:
                        distance=-1
                        elevatorIndex=0
                        while elevator!=None:
                            if elevator.getState==ERROR:
                                elevatorIndex+=1
                                continue
                            if callForElev.getType()==self.upOrDown(elevator):
                                tempDist=self.abDST(elevator.getDST,src)
                                if distance==-1:
                                    distance=tempDist
                                    index=elevatorIndex
                                elif tempDist<distance:
                                        distance=tempDist
                                        index=elevatorIndex
                            elevatorIndex+=1
                return index

#this function insert the calls inside the chosen elevator
    def cmdElevator(self,elevator,callForElev):
        SRC=callForElev.getSrc()
        DST=callForElev.getDST()
        if SRC>DST:
            elevator.getDownCall(callForElev)
        elif DST>SRC:
            elevator.getUpCall(callForElev)
            












                            
                            















