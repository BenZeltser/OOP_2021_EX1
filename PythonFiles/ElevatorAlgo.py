import math
import Elevator
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
        elev=Building.getElevator(elevatorIndex)
        pos=elev.getPos()
        speed=elev.getSpeed()
        startNstop=elev.getStartTime()+elev.getStopTime()
        stopTime=elev.getStopTime()
        state=elev.getState()
        distance=math.fabs((src-pos))
        if src==pos:
            return 0
        if state==0:
            answer=distance*speed+startNstop
        elif state==1 or state==-1:
            answer=distance*speed+stopTime
        return answer


