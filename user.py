from flask import Flask, request, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = 'userdata.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            return 'Username already exists!'

        # If the username is not present, store it in the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        cursor.close()

        return 'User registered successfully!'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)