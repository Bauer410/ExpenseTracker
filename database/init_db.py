import sqlite3

connection = sqlite3.connect('./database/database.db')

with open('./database/expenses.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (20.0, 'Category A', 'This is a description')
            )

cur.execute("INSERT INTO expenses (amount, category, description) VALUES (?, ?, ?)",
            (13.2, 'Category B', 'This is a second description')
            )

connection.commit()
connection.close()
