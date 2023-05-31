from flask import Flask, jsonify, request


from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType


# Create the application instance
app = Flask(__name__)


transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('pizza', 50),
    Expense('Rock Concert', 100)
]


# Create the first route that retuns incomes
@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)


# Create the second route that adds incomes
@app.route('/incomes', methods=['POST'])
def add_incomes():
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return '', 204


# Create the third route that returns expenses
@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)


# Create the fourth route that adds expenses
@app.route('/expenses', methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return '', 204

# Run the application
if __name__ == "__main__":
    app.run(debug=True)