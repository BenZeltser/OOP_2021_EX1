
'''
    Initial Class, classes within the Directory 'PythonFiles' import from this class.
'''

class aBuildingUnit:
    def __init__(self, minFloor, maxFloor, elevators: list):
        self.elevators = elevators
        self.maxFloor = maxFloor
        self.minFloor = minFloor