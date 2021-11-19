import math
import Building
from ElevatorCall import CallForElevator


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






























