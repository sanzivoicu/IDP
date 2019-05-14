from flask import Flask, request
import mysql.connector
import json
import requests
import os
import re
import itertools
import sys

global result
global clients
global fails

app = Flask(__name__)

@app.route("/login")
def login():
    global clients
    global fails

    card_number = request.args.get('cardnumber')
    pin = request.args.get('pin')

    if card_number not in clients:
        clients.append(card_number)
        fails[card_number] = 0

    if fails[card_number] == 3:
        return "Your card in locked"

    response = requests.get("http://172.11.1.2:5000/adminlogin?cardnumber=" + card_number + "&pin=" + pin)

    print(response.content.decode("utf-8"))
    sys.stdout.flush()

    if response.content.decode("utf-8") == "Ok": 
        return "Your login was successful"

    fails[card_number] = fails[card_number] + 1

    if fails[card_number] == 3:
        return "Your card in locked"

    return "Please try again"

@app.route("/logout")
def logout():
    global clients
    global fails

    card_number = request.args.get('cardnumber')

    if card_number not in clients:
        return "You are not logged in"

    if fails[card_number] == 3:
        return "Your card in locked"

    clients.remove(card_number)
    del fails[card_number]

    return "Your logout was successful"

@app.route("/listsold")
def listsold():
    global clients
    global fails

    card_number = request.args.get('cardnumber')  

    if card_number not in clients:
        return "You are not logged in"  

    if fails[card_number] == 3:
        return "Your card in locked"

    response = requests.get("http://172.11.1.2:5000/adminlistsold?cardnumber=" + card_number)
    
    return response.content

@app.route("/withdrawmoney")
def withdrawmoney():
    global clients
    global fails

    card_number = request.args.get('cardnumber')
    amount = request.args.get('amount')    

    if card_number not in clients:
        return "You are not logged in"    

    if fails[card_number] == 3:
        return "Your card in locked"

    response = requests.get("http://172.11.1.2:5000/adminwithdrawmoney?cardnumber=" + card_number + "&amount=" + amount)

    if response.content.decode("utf-8") == "Fail":
        return "You have infsufficient funds in your bank account"

    return "Success"

@app.route("/depositmoney")
def depositmoney():
    global clients
    global fails

    card_number = request.args.get('cardnumber')
    amount = request.args.get('amount')

    if card_number not in clients:
        return "You are not logged in"

    if fails[card_number] == 3:
        return "Your card in locked"

    requests.get("http://172.11.1.2:5000/admindepositmoney?cardnumber=" + card_number + "&amount=" + amount)

    return "Success"

@app.route("/unlock")
def unlock():
    global clients
    global fails

    card_number = request.args.get('cardnumber')
    secret_password = request.args.get('secretpassword')

    response = requests.get("http://172.11.1.2:5000/adminunlock?cardnumber=" + card_number + "&secretpassword=" + secret_password)

    if response.content.decode("utf-8") == "Ok":
        clients.remove(card_number)
        del fails[card_number]
        return "Your account was unlocked, please login again"

    return "Incorrect credentials"

if __name__ == '__main__':
    global clients
    global fails

    clients = []
    fails = {}

    app.run(host='0.0.0.0')
