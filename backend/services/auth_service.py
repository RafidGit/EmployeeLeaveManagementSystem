users = {
    "emp001": {"name": "John", "role": "employee"},
    "mgr001": {"name": "Alice", "role": "manager"}
}

def authenticate(user_id):
    return users.get(user_id)
