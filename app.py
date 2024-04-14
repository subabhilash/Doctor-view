from flask import Flask, jsonify, render_template, request, redirect, url_for
from database import load_db

import mysql.connector
from database import mydb

app = Flask(__name__)

# Hardcoded username and password for simplicity
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# Flag to check if the user is logged in
logged_in = False


@app.route('/')
def home():
  if not logged_in:
    return redirect(url_for('login'))
  patients = load_db()
  return render_template('home.html', patients=patients)


@app.route('/login', methods=['GET', 'POST'])
def login():
  global logged_in
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
      logged_in = True
      return redirect(url_for('home'))
    else:
      return "Invalid username or password"
  return render_template('login.html')


@app.route("/logout")
def logout():
  global logged_in
  logged_in = False
  return redirect(url_for('login'))


@app.route("/submit", methods=["POST"])
def submit_form():
  if not logged_in:
    return redirect(url_for('login'))

  name = request.form["name"]
  age = request.form["age"]
  date = request.form["date"]
  time = request.form["time"]
  tablet = request.form["tablet"]

  cursor = mydb.cursor()
  sql = "INSERT INTO tablets (p_date,p_time,p_name,age,tablet) VALUES (%s, %s, %s, %s, %s)"
  val = (date, time, name, age, tablet)
  cursor.execute(sql, val)
  mydb.commit()

  return "Form submitted successfully"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
