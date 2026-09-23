from flask import Blueprint, request, Flask
from hourcomp import business_bp
from shift import shift_bp

app = Flask(__name__)

app.register_blueprint(business_bp)
app.register_blueprint(shift_bp)


if __name__ == "__main__":
    app.run(debug=True, port= 5001)
