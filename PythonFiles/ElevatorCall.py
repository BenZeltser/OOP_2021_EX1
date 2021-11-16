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
        self.time = 0
        self.SRC = SRC
        self.DST = DST
        self.state=INIT

#this function adds the total time a call is taken
    def addTime(self,newTime):
        self.time=self.time+newTime

#returns the source of the call
    def get_SRC(self):
        return self.SRC

#returns the destantion of the call
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

    def setElevator(self,index):
        elevator=index

    def isDone(self,floor):
        if floor==self.DST:
            return 1
        else
            return 0


