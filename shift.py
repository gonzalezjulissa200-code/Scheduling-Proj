from datetime import datetime
from flask import Blueprint, request, render_template

shift_bp = Blueprint("shifts", __name__)


shiftlist = {}

class shiftMake:
    def __init__(self,start, end, day, capacity):
        self.start = start
        self.end = end
        self.day = day
        self.capacity = int(capacity)
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

    def removeEmp(self, employee):
        if employee in self.empAssigned:
            self.empAssigned.remove(employee)
        else:
            print("cannot remove")

@shift_bp.route("/create-shift", methods=["POST"])
def Shift_Info():
    data = request.get_json()
    starting = data["start"]
    ending = data["end"]
    day = data["day"]
    capacity = data["capacity"]

    shiftnumber = len(shiftlist)
    nextnumber = shiftnumber + 1
    ID_number = str(nextnumber).zfill(4)
    newShift = shiftMake(starting, ending, day, capacity)
    shiftlist[ID_number ] = newShift

    print(ID_number)
    print(newShift.start)
    print(newShift.end)
    print(newShift.day)
    print(newShift.capacity)
    print(newShift.duration)
    return {"status": "ok"}


@shift_bp.route("/")
def home():
    return render_template("index.html", shiftMake = shiftMake)

# shift = shiftMake("04:00", "18:00", 3)

# shift.shiftAssign("employee 1")
# shift.shiftAssign("employee 2")
# shift.shiftAssign("employee 3")
# shift.shiftAssign("employee 4")


# print(shift.empAssigned)

# print(shift.duration)