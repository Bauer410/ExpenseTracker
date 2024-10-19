import sqlite3


class DatabaseManager:
    def get_db_connection(self):
        conn = sqlite3.connect('./database/database.db')
        conn.row_factory = sqlite3.Row
        return conn

    def getAllExpenses(self):
        conn = self.get_db_connection()
        expenses = conn.execute('SELECT * FROM expenses').fetchall()
        conn.close()
        return expenses

    def saveExpense(self, expense):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO expenses (user_id, category_id, amount, description) VALUES (?,?,?,?)',
                     (18, 22, expense.amount, expense.description))
        conn.commit()
        conn.close()

    def deleteExpense(self, expense_id):
        return

    def editExpense(self, expense):
        return
