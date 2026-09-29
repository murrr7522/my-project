from flask import Flask, render_template, request, jsonify
import mysql.connector
import hashlib

app = Flask(__name__)  

@app.route('/user_register', methods=['POST'])
def user_register():
    req = request.get_json()
    cnx = mysql.connector.connect(
        host="185.114.247.43",
        port=3306,
        database="sch688_vvedenie",
        user="sch688_vvedenie",
        password="Qwerty123")
        
    name = req['name']
    login = req['email']
    password = req['password']  
    
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    date = (name, login, hashed_password)
    cur = cnx.cursor()
    try:
        rows = cur.execute('INSERT INTO `users`(`username`, `email`, `password_hash`) VALUES (%s, %s, %s)', date)
    except:
        return {'result': False}
    cnx.commit()
    cnx.close()
    return {'result': True, 'id': cur.lastrowid}
        
        
@app.route('/user_login', methods=['POST'])
def user_login():
    try:
        req = request.get_json()
        cnx = mysql.connector.connect(
            host="185.114.247.43",
            port=3306,
            database="sch688_vvedenie",
            user="sch688_vvedenie",
            password="Qwerty123")
        
        username = req['username']
        password = req['password']
        
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        cur = cnx.cursor(dictionary=True)
        cur.execute('SELECT * FROM `users` WHERE `username` = %s AND `password_hash` = %s', (username, hashed_password))
        user = cur.fetchone()
        cnx.close()
        
        if user:
            return {'result': True, 'id': user['id']}  
        else:
            return {'result': False}
    except Exception as e:
        print('blin:', e)  
        return {'result': False}
    

@app.route("/")
def registration():
    return render_template('registration.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return "<h1>Добро пожаловать!</h1>"

if __name__ == '__main__':
    app.run(debug=True)