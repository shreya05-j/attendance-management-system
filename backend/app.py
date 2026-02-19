from flask import Flask, jsonify
from config import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "Attendance Management System Backend Running"

# Test route to check DB connection
@app.route("/schools")
def get_schools():
    conn = get_db_connection()
    schools = conn.execute("SELECT * FROM schools").fetchall()
    conn.close()
    return jsonify([dict(row) for row in schools])

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/db-path")
def db_path():
    from config import DATABASE
    return DATABASE
