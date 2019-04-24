from flask import Flask, request
import mysql.connector
import json

global cursor
global connection

app = Flask(__name__)

def add_clients():

    cursor = connection.cursor()
    command = 'INSERT INTO Users VALUES(\'Sanziana\', \'Voicu\', \'secret1\', 123456, 1111, 1500)';
    print(command)
    cursor.execute(command)
    command = 'INSERT INTO Users VALUES(\'John\', \'Doe\', \'secretpass1\', 234567, 1234, 500)';
    cursor.execute(command)           
    cursor.close()

@app.route('/History')
def Flights():
    
    global connection
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM History')
    data = cursor.fetchall()

    cursor.close()

    return json.dumps(data, indent = 4)

@app.route('/Users')
def Tickets():
    
    global connection
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Users')
    data = cursor.fetchall()

    cursor.close()

    return json.dumps(data, indent = 4)

if __name__ == '__main__':
    global connection
    
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database' : 'ATM'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    print("Here")
    cursor.execute('DELETE FROM Users')
    cursor.execute('DELETE FROM History')

    add_clients()
    
    cursor.close()

    app.run(host='0.0.0.0')
