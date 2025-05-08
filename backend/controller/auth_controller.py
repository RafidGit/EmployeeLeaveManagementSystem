from flask import Blueprint, request, jsonify
from services.db import get_db_connection

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    employee_id = data.get("employeeId")
    password = data.get("password")

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, role FROM users WHERE employee_id = %s AND password = %s",
                    (employee_id, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            return jsonify({
                "userId": user[0],
                "role": user[1]
            }), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
