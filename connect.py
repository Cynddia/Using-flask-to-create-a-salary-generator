from flask import Flask, request, render_template, redirect, url_for
import pymysql as pms

app = Flask(__name__)
conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="secured",
                   db="employee")

@app.route('/')
def login():
    return render_template('log.html')

@app.route('/', methods=['POST'])
def login_post():
    ename = request.form['ename']
    passcode = request.form['passcode']

    cur = conn.cursor()
    cur.execute("SELECT * FROM login WHERE ename=%s AND passcode=%s", (ename, passcode))
    account = cur.fetchone()

    if account:
        # Login successful
        return redirect(url_for('index'))
    else:
        # Login failed
        return "Invalid username or password"

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
