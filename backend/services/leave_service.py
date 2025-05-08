from .db import get_db_connection

class LeaveService:
    def __init__(self):
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM leave")
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def fetch_by_user(self, user_id):
        self.cursor.execute("SELECT * FROM leave WHERE user_id = %s", (user_id,))
        rows = self.cursor.fetchall()
        return [self._row_to_dict(row) for row in rows]

    def _row_to_dict(self, row):
        return {
            "id": row[0],
            "leave_type": row[1],
            "start_date": row[2],
            "end_date": row[3],
            "total_days": row[4],
            "note": row[5],
            "status": row[6],
            "user_id": row[7]
        }

    def insert(self, data):
        query = """INSERT INTO leave (user_id, leave_type, start_date, end_date, total_days, note, status)
                   VALUES (%s, %s, %s, %s, %s, %s, 'Pending')"""
        self.cursor.execute(query, (
            data["userId"], data["leaveType"], data["startDate"],
            data["endDate"], data["totalDays"], data["note"]
        ))
        self.conn.commit()

    def update(self, id, data):
        self.cursor.execute("""UPDATE leave SET leave_type=%s, start_date=%s, end_date=%s, 
                               total_days=%s, note=%s WHERE id=%s AND status='Pending'""",
            (data["leaveType"], data["startDate"], data["endDate"],
             data["totalDays"], data["note"], id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM leave WHERE id=%s AND status='Pending'", (id,))
        self.conn.commit()

    def update_status(self, id, status):
        self.cursor.execute("UPDATE leave SET status=%s WHERE id=%s", (status, id))
        self.conn.commit()
