#monday through sunday
#from datetime import time
from flask import Flask, request, render_template
app = Flask(__name__)

#create days with an open and close
business_hours = {
    "Monday": {"open": "00:00", "close": "00:00"},
    "Tuesday": {"open": "00:00", "close": "00:00"},
    "Wednesday": {"open": "00:00", "close": "00:00"},
    "Thursday": {"open": "00:00", "close": "00:00"},
    "Friday": {"open": "00:00", "close": "00:00"},
    "Saturday": {"open": "00:00", "close": "00:00"},
    "Sunday": {"open": "00:00", "close": "00:00"},
}

@app.route("/update-hours", methods=["POST"])
def update_hours():
    data = request.get_json()
    day = data["day"]
    field = data["field"]
    time = data["time"]

    business_hours[day][field]= time
    print(business_hours[day])
    return {"status": "ok"}

@app.route("/")
def home():
    return render_template("index.html", business_hours = business_hours)

