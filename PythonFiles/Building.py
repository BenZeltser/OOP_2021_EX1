from typing import List, Any

import Elevator
import ElevatorCall
import ElevatorAlgo


class building(object):

    elevators: list[Any]

    def __init__(self, minFloor,maxFloor,elevators):
        self.elevators=elevators
        self.maxFloor = maxFloor
        self.minFloor=minFloor