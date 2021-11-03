import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db", user="max_twain", password="password", host="localhost", port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    if username and password:
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND passworld=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        if records:
            return render_template('account.html', full_name=records[0][1], log_pass=username+":"+password)
        else:
            return '<p> Вы не существуете <p>'
    return '<p> Отсутствие логина или пароля <p>'

