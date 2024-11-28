from typing import List

from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.DatabaseManager import DatabaseManager
from model.Expense import ExpenseDto, ExpenseModel

app = Flask(__name__, static_folder='templates', static_url_path='/static')
db = DatabaseManager()
app.secret_key = "secret_key"  # Necessary for using flash messages


@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    dbUser = db.getUserByUsername(session['username'])
    expenses: List[ExpenseModel] = []
    expensesAllUsers = db.getUserExpenses()
    for expense in expensesAllUsers:
        if expense['username'] == dbUser['username']:
            model = ExpenseModel(expense['username'], expense['category_name'], expense['amount'],
                                 expense['description'])
            expenses.append(model)

    return render_template('index.html', expenses=expenses, total_expenses=db.getTotalExpenses(dbUser['user_id']))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        flash("Login successful", "success")
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/loginVerify', methods=['POST'])
def login_verify():
    username = request.form['username']
    password = request.form['password']
    dbUser = db.getUserByUsername(username)

    # Check if the username and password match
    if dbUser['username'] == username and dbUser['password_hash'] == password:
        session['username'] = username
        flash("Login successful", "success")
        return redirect(url_for('index'))
    else:
        flash("Invalid credentials", "error")
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out", "success")
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        db.addUser(username, email, password)
        session['username'] = request.form['username']
        flash('Sign up successful! Redirecting to the main page.', 'success')
        return redirect(url_for('index'))
    return render_template('signup.html')


@app.route("/addExpense", methods=['POST'])
def add_expense():
    if 'username' not in session:
        flash("You need to log in first", "error")
        return redirect(url_for('login'))

    dbUser = db.getUserByUsername(session['username'])

    description = request.form.get('description')
    amount = request.form.get('amount')
    category = request.form.get('category')
    expense = ExpenseDto(dbUser['user_id'], category, float(amount), description)
    db.saveExpense(expense)

    flash("Expense added successfully!", "success")
    return redirect(url_for('index'))


def function_to_test(x):
    return x * x


if __name__ == '__main__':
    app.run(debug=True)
