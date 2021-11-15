from typing import Iterable, Union, Tuple, Any, Type

import static
from DoubleLinkedList import DoubleLinkedList, Node


# Columns:
# 1 - same String as always
# 2 - Time
# 3 - SRC
# 4 - DST
# 5 NOT RELEVANT
# 6 - THE INDEXED ELEVATOR TO ALLOCATE 4 THE CALL

class Elevator:
    global ERROR, DOWN, LEVEL, UP, OPEN, CLOSE
    ERROR = -2
    DOWN = -1
    LEVEL = 0
    UP = 1
    OPEN = 1
    CLOSE = 0

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime

        self.state = LEVEL
        self.currentFloor = Node(self._minFloor)

        '''
        Initiate a Doubly Linked List 
        '''
        # init floorSet
        curr = self.currentFloor
        self.floorSet = DoubleLinkedList(curr)

        i = curr.get_data()
        while i < self._maxFloor:
            self.floorSet.insert_end(curr.get_data() + i)
            i += 1

        '''
        Send the Node curr back to 0
        '''
        temp = self.currentFloor
        while temp.get_data() > 0:
            temp = temp.get_prev()
        self.currentFloor=temp

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
        return self.currentFloor.get_data()

    def getState(self):
        return self.state
        #Return level by default
