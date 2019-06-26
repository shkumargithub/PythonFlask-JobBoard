from flask import Flask, render_template, g
import sqlite3

PATH = "db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', None)
    if connection == None:
        connection = g._connection = sqlite3.conect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, signle=False):
    connection = open_connection()
    cursor =  connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection =  getattr(g, '_connection', None)
    if connection is not None:
        connection.close()

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")
