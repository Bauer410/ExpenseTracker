import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('./database/database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def hello_world():
    conn = get_db_connection()
    expenses = conn.execute('SELECT * FROM expenses').fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)


if __name__ == '__main__':
    app.run()
