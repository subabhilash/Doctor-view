from flask import Flask, jsonify, render_template
from database import load_db

from flask import request
import mysql.connector
from database import mydb

app = Flask(__name__)


@app.route('/')
def hello_world():
  patients = load_db()
  return render_template('home.html',
                        patients=patients
                        )

@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form["name"]
    age = request.form["age"]
    date = request.form["date"]
    time = request.form["time"]
    tablet = request.form["tablet"]

    cursor = mydb.cursor()
    sql = "INSERT INTO tablets (p_date,p_time,p_name,age,tablet) VALUES (%s, %s, %s, %s, %s)"
    val = (date, time,name, age, tablet)
    cursor.execute(sql, val)
    mydb.commit()

    return "Form submitted successfully"





if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
