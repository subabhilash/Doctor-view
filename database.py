import os
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
    host="database-1.cjcyeqckaoos.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="abhilash",
    port=3306,
    database="patient_database")

def load_db():
  #Get data
  sql = "SELECT * FROM patients;"
  mycursor = mydb.cursor()
  mycursor.execute(sql)
  myresult = mycursor.fetchall()


  # Define a function to convert tuples to dictionaries
  def tuple_to_dict(cursor, row):
      return dict(zip(cursor.column_names, row))

  # Convert the result into a list of dictionaries
  myresult_dict = [tuple_to_dict(mycursor, row) for row in myresult]
  return myresult_dict





