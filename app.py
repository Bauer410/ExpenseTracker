from flask import Flask, render_template, request, redirect

from database.DatabaseManager import DatabaseManager
from model.Expense import ExpenseDto

app = Flask(__name__)
db = DatabaseManager()


@app.route('/')
def index():
    expenses = db.getAllExpenses()
    if len(expenses) > 0:
        print("There are this number of expenses in database: ")
        print(len(expenses))
    return render_template('index.html', expenses=db.getAllExpenses())

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/loginVerify', methods=['POST'])
def loginVerify():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    return render_template('index.html')

@app.route("/addExpense", methods=['POST'])
def addExpense():
    description = request.form.get('description')
    amount = request.form.get('amount')
    category = request.form.get('category')
    expense = ExpenseDto(11, category, float(amount), description)
    db.saveExpense(expense)
    return redirect("/")

def functionToTest(x):
    return x*x

if __name__ == '__main__':
    app.run()
