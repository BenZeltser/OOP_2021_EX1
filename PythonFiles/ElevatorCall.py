# *
# * This interface represents a call for an elevator - with a dedicated destination (aka smart Elevators).
# * The call has few states: {Init, Going2SRC, Going2Dest, Done}, each state has a time stamp (in seconds).
#
class CallForElevator(object):
    INIT = 0
    GOING2SRC = 1
    GOING2DEST = 2
    DONE = 3
    UP = 1
    DOWN = -1

    global time
    global SRC
    global DST

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
        pass
    #    * Returns the time (in second) of the given state, if "not there yet" returns -1
    #     * @param state - the int representing the state for which the time stamp is requested.

    # * @return the destination floor to which this elevator call is targeted to.
    def getDest(self):
        pass

    # * @return the type of this call {UP,DOWN};
    def getType(self):
        pass

    # * This methods return the index of the Elevator in the building to which this call was assigned to, if not yet
    # Assigned --> return -1
    def allocatedTo(self):
        pass
