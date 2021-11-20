import heapq
import math
from ElevatorCall import CallForElevator
import BuildingObject as building

class elevatorAlgo:
    global ERROR, DOWN, LEVEL, UP, GOING2SRC, GOING2DST, DONE
    ERROR = -2
    DOWN = -1
    LEVEL = 0
    UP = 1
    GOING2SRC = 1
    GOING2DST = 2
    DONE = 3

    def __init__(self, building: object):
        self.building = building

    # returns the building the algorithm is currently working on
    def getBuilding(self):
        return self.building


    def singleElevatorAllocation(self, abuilding: building.aBuildingUnit, calls: list[CallForElevator]):
        allCalls = []
        for call in calls:
            allCalls.append(calls[call].get_SRC())
            heapq.heapify(calls)
        elevators = building.aBuildingUnit.elevators
        for call in allCalls:
            currentPos = elevators[0].getPos()
            for elevator in elevators:
                if (elevator.getPos() < currentPos):
                    currentPos = elevator.getPos()
                elevators[currentPos].goto(call.get_SRC())

    def getUpElevators(self,indexList: list):
        size=len(indexList)
        upList=[]
        if int(size)%2==1:
            divider=int((size-1)/2)
            index=0
            for i in range(1,divider):
                upList.append(indexList[index])
                index=index+2
            upList.append(indexList[index])
        else:
            divider=int(size/2)
            index=0
            for i in range(0,divider):
                upList.append(indexList[index])
                index=index+2
        return upList

    def getDownElevators(self,indexList: list):
        size=len(indexList)
        downList=[]
        if int(size)%2==1:
            divider=int((size-1))/2
            index=1
            for i in range(0,divider):
                downList.append(indexList[index])
                index=index+2
        else:
            divider=int(size/2)
            index=1
            for i in range(0,divider):
                downList.append(indexList[index])
                index=index+2
        return downList

    def divideFloors(self,abuilding: building.aBuildingUnit, param):
        floors=[]
        min=abuilding.minFloor
        max=abuilding.maxFloor
        size=math.fabs(max-min)
        divide=int(size/param)
        floor=max
        for i in range(0,param):
            floors.append(floor)
            floor=floor+divide
        return floors

    def ChooseElevator(self,src,dst,floors,upCalls,downCalls,flag):
        index=1
        direction=0
        if int(src)>int(dst):
            direction=-1
        elif int(dst)>int(src):
            direction=1

        while(index<len(floors)):
            if int(src)<floors[index]:
                if direction==1:
                    if flag != -1:
                        if index == 1:
                            if flag == 0:
                                return upCalls[0]
                            else:
                                return upCalls[1]
                        else:
                            return upCalls[index]
                    else:
                        return upCalls[index-1]
                elif direction==-1:
                    return downCalls[index-1]
            index+=1
        if direction==1:
            if flag!=-1:
                return upCalls[index]
            else:

                return upCalls[index-1]
        else:
            return downCalls[index-1]




































