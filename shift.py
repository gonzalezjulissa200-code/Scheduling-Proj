from datetime import datetime

class shiftMake:
    def __init__(self,start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.empAssigned = []

        self.shiftduration()

    def shiftduration(self):
        starttime = self.start
        starttime = datetime.strptime(starttime, "%H:%M")
        endtime = self.end
        endtime = datetime.strptime(endtime, "%H:%M")
        duration = endtime - starttime
        self.duration = duration

    def shiftAssign(self, assigned):
        if len(self.empAssigned) < self.capacity:
            self.empAssigned.append(assigned)
        else:
            print("not allowed")

shift = shiftMake("04:00", "18:00", 3)

shift.shiftAssign("employee 1")
shift.shiftAssign("employee 2")
shift.shiftAssign("employee 3")
shift.shiftAssign("employee 4")


print(shift.empAssigned)

print(shift.duration)