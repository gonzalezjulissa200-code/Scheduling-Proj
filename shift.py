from datetime import datetime

class shiftMake:
    def __init__(self,start, end, capacity):
        self.start = start
        self.end = end
        self.shiftduration()
        self.capacity = capacity
        self.empAssigned = []

    def shiftduration(self):
        starttime = self.start
        starttime = datetime.strptime(starttime, "%H:%M")
        endtime = self.end
        endtime = datetime.strptime(endtime, "%H:%M")
        duration = endtime - starttime
        self.duration = duration

    def shiftCap(assigned, max):
        self.capacity = max
        self.empAssigned = []
        if len(self.empAssigned) < self.capacity:
            self.empAsssigned.append(assigned)
        else:
            print("not allowed")

shift = shiftMake("04:00", "18:00")


print(shift.duration)