from flask import Flask, redirect, request
import pymysql
app = Flask(__name__)

connection = pymysql.connect(host='database-1.c65uwrrkzb8g.us-east-1.rds.amazonaws.com', port=3306,
                             user='admin', passwd='Aa123123', db='aviel', autocommit=True)

def show_animals(cursor_to_execute):
    cursor_to_execute.execute("select * from animals")
    result = []
    for row in cursor_to_execute:
        result.append(row[0])
    return result


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    cursor1 = connection.cursor()
    if request.method == 'GET':
        return str(show_animals(cursor1))
    elif request.method == 'POST':
        return 'creating your name'


app.run(host="0.0.0.0", port=5001, debug=True)
