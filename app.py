from flask import Flask,render_template,request,redirect
import sqlite3



def getDB():
    conn = sqlite3.connect('example.db')
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    cursor = getDB()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
    )
    ''')
    return render_template('index.html')


@app.route('/submit',methods = ['POST'])
def enter_into_db():
    conn = getDB()
    cursor = conn.cursor()
    name = request.form['name']
    age = request.form['age']
    query = '''
    INSERT INTO users (name, age) VALUES (?, ?)
    '''
    cursor.execute(query, (name, age))
    conn.commit()
    return redirect('/')

@app.route('/display',methods = ['GET'])
def display_all_data():
    cursor = getDB().cursor()
    query = '''
    SELECT * FROM users
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('display.html',data = data)

@app.route('/display_one/<name>',methods = ['GET'])
def display_one(name):
    cursor = getDB().cursor()
    cursor.execute(''' SELECT * from users where name = ?  ''',(name,))
    data = cursor.fetchall()
    return render_template('display.html',data = data)

@app.route('/something_new')
def some():
    return 'work under process'

if __name__ == '__main__':
    app.run(debug=True)

