import math
import Building




class elevatorAlgo:

    global ERROR, DOWN, LEVEL, UP,GOING2SRC, GOING2DST, DONE, elevatorList
    ERROR= -2
    DOWN = -1
    LEVEL = 0
    UP = 1
    GOING2SRC=1
    GOING2DST=2
    DONE=3
    elevatorList = []

    def __init__(self, building: object):
        self.building = building

    def getBuilding(self):
        return self.building

    @staticmethod
    def algoName():
        return "EX1_OOP_Smart_Elevator_Algo_Offline"


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

    def addCall (self, elevatorCall):
        elevatorList.append(self, elevatorCall)

    @staticmethod
    def removeCalls(self):
        index=0
        while index<len(elevatorList):
            if elevatorList(index).getState()==DONE:
                elevatorList.remove(index)
                continue
            index+=1

    def allocateAnElevator(self,callForElev):
        elevatorAlgo.removeCalls()
        index=-1
        elevatorIndex=0
        src=callForElev.getSrc()
        distance=-1
        elevator= Building.getElevator(index)
        while elevator!=None
            if elevator.getState()==ERROR
                index+=1
                continue
            pos=elevator.getPos()
            if self.isValid(elevator.getState(),src,elevator.getCallType())==True
                tempdist=self.distance(index,src)
                if tempdist!=-1
                        if tempdist==0
                            self.addCall(callForElev)
















