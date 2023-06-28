from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
import json
import random


from classes.User import User
from models.finalmodel import model

app = Flask(__name__)

load_dotenv()


app.config["MYSQL_USER"] = os.getenv("USER")
app.config["MYSQL_PASSWORD"] = os.getenv("PASSWORD")
app.config["MYSQL_DB"] = os.getenv("DATABASE")


mysql = MySQL(app)


@app.route('/signup')
def signup():
    cur = mysql.connection.cursor()
    data = json.loads(request.data)
    username = str(data['username'])
    password = str(data['password'])
    id = ""
    for i in range(50):
        id += (str(random.randint(0, 9)))
    requestedUser = User(id, username, password)
    try:
        cur.execute("INSERT INTO users(UserID,username,password) VALUES(%s,%s,%s)",
                    (requestedUser.userID, requestedUser.username, requestedUser.password))
        mysql.connection.commit()
        cur.close()
        response = make_response(jsonify(status='success',), 201)
        return response
    except:
        cur.close()
        response = make_response(jsonify(
            status='fail',
            message='Username already in use'
        ), 401)
        return response


@app.route('/login')
def login():
    cur = mysql.connection.cursor()
    data = json.loads(request.data)
    username = str(data['username'])
    password = str(data['password'])
    print(username)
    print(password)

    cur.execute("SELECT * from users")
    rv = cur.fetchall()
    cur.close()
    for tuple in rv:
        if tuple[1] == username:
            if password == tuple[2]:
                response = make_response(jsonify(
                    status='success', userID=tuple[0], username=tuple[1], message='Login successful'), 200)
                return response
            else:
                response = make_response(
                    jsonify(status='fail', message='Password incorrect'), 401)
                return response
    response = make_response(jsonify(
        status='fail', message='No user exists with this username. Please sign up.'), 404)
    return response


@app.route('/users')
def getUsers():
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM USERS''')
        rv = cur.fetchall()
        cur.close()
        cleanedrv = []
        for tuple in rv:
            cleanedrv.append({
                'userID': tuple[0],
                'username': tuple[1]
            }
            )
        response = make_response(jsonify(cleanedrv), 200)
        return response
    except:
        response = make_response(
            jsonify(status='fail', message='An error has occurred. Please try again.'), 400)
        return response


@app.route('/estimations/<userid>')
def getEstimationsByUser(userid):
    id = str(userid)
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * from ''')


@app.route('/addestimation')
def addEstimation():
    data = json.loads(request.data)
    contract_start = float(data['CONTRACT_START'])
    age = float(data['AGE'])
    min = float(data['MIN'])
    pts = float(data['PTS'])
    fgm = float(data['FGM'])
    fga = float(data['FGA'])
    threePM = float(data['3PM'])
    threePA = float(data['3PA'])
    ftm = float(data['FTM'])
    fta = float(data['FTA'])
    reb = float(data['REB'])
    ast = float(data['AST'])
    tov = float(data['TOV'])
    stl = float(data['STL'])
    blk = float(data['BLK'])
    pf = float(data['PF'])
    print(model(contract_start, age, min, pts, fgm, fga, threePM,
          threePA, ftm, fta, reb, ast, tov, stl, blk, pf))
    return 'ok'


if __name__ == "__main__":
    app.run()
