from flask import Flask, render_template, request, redirect, url_for, flash, session
from database.DatabaseManager import DatabaseManager
from model.Expense import ExpenseDto

app = Flask(__name__, static_folder='templates', static_url_path='/static')
db = DatabaseManager()
app.secret_key = "secret_key"  # Necessary for using flash messages

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    expenses = []
    if not app.debug:
        expenses = db.getUserExpenses()

    return render_template('index.html', expenses=expenses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Automatically log in without checking credentials
        session['username'] = request.form['username']
        flash("Login successful", "success")
        return redirect(url_for('index'))
    return render_template('Login.html')

@app.route('/loginVerify', methods=['POST'])
def login_verify():
    return login()

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out", "success")
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Dummy action to redirect to the main page after signup
        flash('Sign up successful! Redirecting to the main page.', 'success')
        return redirect(url_for('index'))
    return render_template('SignUp.html')

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
    flash("Expense added successfully!", "success")
    return redirect(url_for('index'))

def function_to_test(x):
    return x * x

if __name__ == '__main__':
    app.run(debug=True)
