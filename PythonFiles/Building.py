import array


class Building():
    ##data
    a_list: list

    def __init__(self, maxFloor, minFloor, elevators):
        self.maxFloor=maxFloor
        self.minFloor=minFloor
        self.elevators = elevators

    def getMaxFloor(self):
        return self.maxFloor

    def getMinFloor(self):
        return self.minFloor


