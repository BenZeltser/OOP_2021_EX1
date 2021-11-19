from typing import Iterable, Union, Tuple, Any, Type


class Elevator():

    def __init__(self, _id, _speed, _minFloor,_maxFloor,_closeTime,_openTime,_startTime,_stopTime):
        self._id=_id
        self._speed=_speed
        self._minFloor=_minFloor
        self._maxFloor=_maxFloor
        self._closeTime=_closeTime
        self._openTime=_openTime
        self._startTime=_startTime
        self._stopTime=_stopTime

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

