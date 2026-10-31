
import os
import sqlite3
from contextlib import contextmanager

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

# Initialize Flask application
app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "local-development-key"
)

# Configure database location
app.config["DATABASE"] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "students.db"
)



@contextmanager
def get_db():

    db = sqlite3.connect(app.config["DATABASE"])
    db.row_factory = sqlite3.Row

    try:
        yield db
        db.commit()

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()



# Create student table
def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_number TEXT UNIQUE NOT NULL,
                course TEXT NOT NULL
            )
        """)


# Home page: Display and search students
@app.route("/")
def index():

    search = request.args.get("search", "").strip()

    with get_db() as db:
        students = db.execute("""
            SELECT * FROM students
            WHERE name LIKE ?
            OR roll_number LIKE ?
            ORDER BY id DESC
        """, (f"%{search}%", f"%{search}%")).fetchall()

    return render_template(
        "index.html",
        students=students,
        search=search
    )


# Add a new student
@app.route("/add", methods=["POST"])
def add_student():

    name = request.form.get("name", "").strip()
    roll = request.form.get("roll_number", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not roll or not course:
        flash("Please fill in all fields.")
        return redirect(url_for("index"))

    try:
        with get_db() as db:
            db.execute("""
                INSERT INTO students
                (name, roll_number, course)
                VALUES (?, ?, ?)
            """, (name, roll, course))

        flash("Student added successfully!")

    except sqlite3.IntegrityError:
        flash("This roll number already exists.")

    return redirect(url_for("index"))


# Delete a student
@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    with get_db() as db:
        db.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

    flash("Student deleted successfully!")

    return redirect(url_for("index"))


# Start application
if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
