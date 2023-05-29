from flask import Flask, jsonify, request

# Create the application instance
app = Flask(__name__)


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]

# Create the first route that retuns incomes
@app.route('/incomes')
def get_income():
    return jsonify(incomes)


# Create the second route that adds incomes
@app.route('/incomes', methods=['POST'])
def add_incomes():
    incomes.append(request.get_json())
    return '', 204


# Run the application
if __name__ == "__main__":
    app.run(debug=True)