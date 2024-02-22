import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = 'CloudEdgeAssignment-database.db'


@app.route("/")
def index():
    return render_template('welcome.html')


@app.route("/login", methods=["GET"])
def login():
    return render_template("register.html")


@app.route("/register_page", methods=["GET"])
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    new_user = "INSERT INTO users (user_name, password) VALUES (?, ?)"
    cursor.execute(new_user, (username, password))
    connection.commit()
    connection.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)