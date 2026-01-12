from flask import Flask, render_template, request, redirect, session
import sqlite3
from auth import authenticate
from logs import init_db

app = Flask(__name__)
app.secret_key = "soc_secret_key"

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ip = request.remote_addr

        success, message = authenticate(username, password, ip)
        if success:
            session["admin"] = True
            return redirect("/dashboard")

    return render_template("login.html", message=message)

@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect("/")

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY id DESC")
    logs = c.fetchall()
    conn.close()

    return render_template("dashboard.html", logs=logs)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
