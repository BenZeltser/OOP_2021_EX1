import array


class Building():

    def __init__(self, maxFloor, minFloor, elevators: list):
        self.maxFloor=maxFloor
        self.minFloor=minFloor
        self.elevators = elevators

    def getMaxFloor(self):
        return self.maxFloor

    def getMinFloor(self):
        return self.minFloor

    def getElevator(self,index):
        return self.elevators[index]


