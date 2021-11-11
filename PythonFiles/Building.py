import array


class Building():
    def __init__(self, maxFloor, minFloor, elevtors: list):
        self.maxFloor=maxFloor
        self.minFloor=minFloor
        self.elevators = elevtors

    def getMaxFloor(self):
        return self.maxFloor

    def getMinFloor(self):
        return self.minFloor


