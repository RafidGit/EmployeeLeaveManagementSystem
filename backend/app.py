from flask import Flask
from flask_cors import CORS
from controller.leave_controller import leave_bp
from controller.auth_controller import auth_bp
from controller.leave_controller import leave_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(leave_bp, url_prefix="/api")

@app.route("/")
def home():
    return {"message": "Leave Management API running"}

if __name__ == "__main__":
    app.run(debug=True)
