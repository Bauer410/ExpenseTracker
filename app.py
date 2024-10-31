from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.DatabaseManager import DatabaseManager
from model.Expense import ExpenseDto

app = Flask(__name__, static_folder='templates', static_url_path='/static')
db = DatabaseManager()
app.secret_key = "secret_key"  # Necessary for using flash messages

@app.route('/')
def index():
    if 'username' not in session:
        flash("You need to log in first", "error")
        return redirect(url_for('login'))
    
    expenses = db.getAllExpenses()
    if len(expenses) > 0:
        print("There are this number of expenses in database: ")
        print(len(expenses))
    return render_template('index.html', expenses=expenses)

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/loginVerify', methods=['POST'])
def login_verify():
    username = request.form['username']
    password = request.form['password']
    
    # Sample user data for demonstration
    users = {
        "test": "password",
    }
    
    # Check if the username and password match
    if users.get(username) == password:
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

@app.route("/addExpense", methods=['POST'])
def add_expense():
    if 'username' not in session:
        flash("You need to log in first", "error")
        return redirect(url_for('login'))
    
    description = request.form.get('description')
    amount = request.form.get('amount')
    category = request.form.get('category')
    expense = ExpenseDto(11, category, float(amount), description)
    db.saveExpense(expense)
    return redirect(url_for('index'))

def function_to_test(x):
    return x * x

if __name__ == '__main__':
    app.run() 