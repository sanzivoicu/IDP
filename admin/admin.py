from flask import Flask, request
import mysql.connector
import json

global cursor
global connection

app = Flask(__name__)

@app.route("/adminlogin")
def login():
    card_number = request.args.get('cardnumber')
    pin = request.args.get('pin')

    cursor = connection.cursor(buffered=True)
    command = 'SELECT * FROM Users where cardnumber = {0} and pin={1}'.format(card_number, pin)

    cursor.execute(command)
    data = cursor.fetchall()
    cursor.close()

    if len(data) == 0:
        return "Fail"

    return "Ok"

@app.route("/adminlistsold")
def listsold():
    card_number = request.args.get('cardnumber')

    cursor = connection.cursor(buffered=True)
    command = 'SELECT * FROM Users where cardnumber = \'{0}\''.format(card_number)

    cursor.execute(command)
    data = cursor.fetchall()
    cursor.close()

    for (_, _, _, _, _, a) in data:
        result = a

    return str(result)

@app.route("/adminwithdrawmoney")
def withdrawmoney():
    amount = request.args.get('amount')
    card_number = request.args.get('cardnumber')

    cursor = connection.cursor(buffered=True)
    command = 'SELECT * FROM Users where cardnumber = \'{0}\''.format(card_number)

    cursor.execute(command)
    data = cursor.fetchall()

    for (_, _, _, _, _, a) in data:
        total = a

    if int(total) < int(amount):
        return "Fail"

    new_total = int(total) - int(amount)
    command = 'UPDATE Users SET amount = {0} WHERE cardnumber = \'{1}\''.format(new_total, card_number)
    cursor.execute(command)

    cursor.close()
    return "Ok"

@app.route("/admindepositmoney")
def depositmoney():
    amount = request.args.get('amount')
    card_number = request.args.get('cardnumber')

    cursor = connection.cursor(buffered=True)
    command = 'SELECT * FROM Users where cardnumber = \'{0}\''.format(card_number)

    cursor.execute(command)
    data = cursor.fetchall()

    for (_, _, _, _, _, a) in data:
        total = a

    new_total = int(total) + int(amount)
    command = 'UPDATE Users SET amount = {0} WHERE cardnumber = \'{1}\''.format(new_total, card_number)
    cursor.execute(command)
    
    cursor.close()
    return "Ok"

@app.route("/adminunlock")
def unlock():
    card_number = request.args.get('cardnumber')
    secret_password = request.args.get('secretpassword')

    cursor = connection.cursor(buffered=True)
    command = 'SELECT * FROM Users where cardnumber = {0} and secretPassword=\'{1}\''.format(card_number, secret_password)

    cursor.execute(command)
    data = cursor.fetchall()
    cursor.close()

    if len(data) == 0:
        return "Fail"

    return "Ok"


def add_clients():

    cursor = connection.cursor()
    command = 'INSERT INTO Users VALUES(\'Sanziana\', \'Voicu\', \'secret1\', 123456, 1111, 1500)';
    print(command)
    cursor.execute(command)
    command = 'INSERT INTO Users VALUES(\'John\', \'Doe\', \'secretpass1\', 234567, 1234, 500)';
    cursor.execute(command)           
    cursor.close()

@app.route('/History')
def History():
    
    global connection
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM History')
    data = cursor.fetchall()

    cursor.close()

    return json.dumps(data, indent = 4)

@app.route('/Users')
def Users():
    
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

    cursor.execute('DELETE FROM Users')
    cursor.execute('DELETE FROM History')

    add_clients()
    
    cursor.close()

    app.run(host='0.0.0.0')
