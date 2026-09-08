#monday through sunday
#from datetime import time
from flask import Flask, request, render_template
app = Flask(__name__)

#create days with an open and close
business_hours = {
    "Monday": {"open": "07:00", "close": "23:00"},
    "Tuesday": {"open": "07:00", "close": "23:00"},
    "Wednesday": {"open": "07:00", "close": "23:00"},
    "Thursday": {"open": "07:00", "close": "23:00"},
    "Friday": {"open": "07:00", "close": "21:00"},
    "Saturday": {"open": "12:00", "close": "17:00"},
    "Sunday": {"open": "12:00", "close": "17:00"},
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

if __name__ == "__main__":
    app.run(debug=True, port= 5001)
