from flask import Blueprint, request, jsonify
from services.leave_service import LeaveService
from services.auth_service import authenticate

leave_bp = Blueprint("leave", __name__)
leave_service = LeaveService()

@leave_bp.route("/login", methods=["POST"])
def login():
    user = authenticate(request.json.get("userId"))
    if not user:
        return jsonify({"error": "Invalid ID"}), 401
    return jsonify(user)

@leave_bp.route("/leaves", methods=["GET"])
def get_leaves():
    role = request.headers.get("role")
    user_id = request.headers.get("userId")
    if role == "manager":
        return jsonify(leave_service.fetch_all())
    return jsonify(leave_service.fetch_by_user(user_id))

@leave_bp.route("/leave", methods=["POST"])
def save_leave():
    data = request.get_json()
    leave_service.insert(data)
    return jsonify({"message": "Leave saved"}), 201

@leave_bp.route("/leave/<int:id>", methods=["PUT"])
def update_leave(id):
    data = request.get_json()
    leave_service.update(id, data)
    return jsonify({"message": "Leave updated"}), 200

@leave_bp.route("/leave/<int:id>", methods=["DELETE"])
def delete_leave(id):
    leave_service.delete(id)
    return jsonify({"message": "Leave deleted"}), 200

@leave_bp.route("/leave/status/<int:id>", methods=["PUT"])
def update_status(id):
    status = request.get_json()["status"]
    leave_service.update_status(id, status)
    return jsonify({"message": "Status updated"}), 200
