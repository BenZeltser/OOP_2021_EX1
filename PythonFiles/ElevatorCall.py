class CallForElevator(object):
    global INIT, GOING2SRC, GOING2DEST, DONE, DOWN, UP

    INIT = 0
    GOING2SRC = 1
    GOING2DEST = 2
    DONE = 3
    UP = 1
    DOWN = -1

    global time, SRC, DST

    def __init__(self, time, SRC, DST):
        self.time = time
        self.SRC = SRC
        self.DST = DST

    def get_time(self):
        return self.time

    def get_SRC(self):
        return self.SRC

    def get_DST(self):
        return self.DST

    # * returns this call current state.
    def getState(self):
        return self.getState()

    # * @return the type of this call {UP,DOWN};

    def getType(self):
        if self.get_SRC() == self.getState():
            pass
        if self.get_SRC() > self.getState():
            return self.UP
        if self.get_SRC() < self.getState():
            return self.DOWN

    # * This methods return the index of the Elevator in the building to which this call was assigned to, if not yet
    # Assigned --> return -1
    def allocatedTo(self):
        pass
