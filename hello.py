"""
We will use this file to check if Flask was correctly installed, we don't 
need to nest it in a new directory.
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! This is a test file"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)