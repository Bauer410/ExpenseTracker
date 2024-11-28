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
        cat_id = self.addCategory(expense.category)
        conn.execute('INSERT INTO expenses (user_id, category_id, amount, description) VALUES (?,?,?,?)',
                     (expense.user_id, cat_id['category_id'], expense.amount, expense.description))
        conn.commit()
        conn.close()

    def deleteExpense(self, expense_id):
        conn = self.get_db_connection()
        conn.execute('DELETE FROM expenses WHERE expense_id = ?', (expense_id,))
        conn.commit()
        conn.close()

    def editExpense(self, expense):
        return

    def getAllCategories(self):
        conn = self.get_db_connection()
        categories = conn.execute('SELECT * FROM categories').fetchall()
        conn.close()
        return categories

    def addCategory(self, category_name):
        conn = self.get_db_connection()
        cat_id = conn.execute('SELECT * FROM categories WHERE category_name = ?', (category_name,)).fetchone()
        if cat_id is None:
            conn.execute('INSERT INTO categories (category_name) VALUES (?)', (category_name,))
            conn.commit()
            cat_id = conn.execute('SELECT * FROM categories WHERE category_name = ?', (category_name,)).fetchone()
        conn.close()
        return cat_id

    def getTotalExpenses(self, user_id):
        conn = self.get_db_connection()
        if user_id:
            total = conn.execute('SELECT SUM(amount) FROM expenses WHERE user_id = ?', (user_id,)).fetchone()[0]
        else:
            total = conn.execute('SELECT SUM(amount) FROM expenses').fetchone()[0]
        conn.close()
        return total if total else 0

    def addUser(self, username, email, password_hash):
        conn = self.get_db_connection()
        conn.execute('INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                     (username, email, password_hash))
        conn.commit()
        conn.close()

    def getUserByUsername(self, username):
        conn = self.get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.commit()
        conn.close()
        return user

    def getAllUsers(self):
        conn = self.get_db_connection()
        users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return users

    # this is for getting expense analysis from view

    def getUserExpenses(self):
        conn = self.get_db_connection()
        user_expenses = conn.execute('SELECT * FROM user_expenses').fetchall()
        conn.close()
        return user_expenses

    def getTotalExpensesByUser(self):
        conn = self.get_db_connection()
        total_expenses_by_user = conn.execute(
            'SELECT users.username, SUM(expenses.amount) AS total_spent FROM expenses '
            'JOIN users ON expenses.user_id = users.user_id '
            'GROUP BY users.username'
        ).fetchall()
        conn.close()
        return total_expenses_by_user

    def getTotalExpensesByCategory(self):
        conn = self.get_db_connection()
        total_expenses_by_category = conn.execute(
            'SELECT categories.category_name, SUM(expenses.amount) AS total_spent FROM expenses '
            'JOIN categories ON expenses.category_id = categories.category_id '
            'GROUP BY categories.category_name'
        ).fetchall()
        conn.close()
        return total_expenses_by_category

    def clearAllExpenses(self):
        # This method is no longer used to clear expenses on refresh
        conn = self.get_db_connection()
        conn.execute('DELETE FROM expenses')
        conn.commit()
        conn.close()
