from typing import Iterable, Union, Tuple, Any, Type

import static

#Colums:
#1 - same String as always
#2 - Time
#3 - SRC
#4 - DST
#5 NOT RELEVANT
#6 - THE INDEXED ELEVATOR TO ALLOCATE 4 THE CALL

class Elevator():


    def __init__(self, _id, _speed, _minFloor,_maxFloor,_closeTime,_openTime,_startTime,_stopTime, upcalls=[],downcalls=[], state):
        self._id=_id
        self._speed=_speed
        self._minFloor=_minFloor
        self._maxFloor=_maxFloor
        self._closeTime=_closeTime
        self._openTime=_openTime
        self._startTime=_startTime
        self._stopTime=_stopTime
        self.downcalls=downcalls
        self.upcalls = upcalls
        self.state = state

    def getID(self):
        return self._id

    def getSpeed(self):
        return self._speed

    def getMinFloor(self):
        return self._minFloor

    def getMaxFloor(self):
        return self._maxFloor

    def getCloseTime(self):
        return self._closeTime

    def getOpenTime(self):
        return self._openTime

    def getStartTime(self):
        return self._startTime

    def getStopTime(self):
        return self._stopTime

    def getPos(self):
        return 0; #PLACEHOLDER

    def getState(self):
        return self.state

    def getUpCalls(self):
        return self.upcalls

    def getDownCalls(self):
        return self.downcalls

