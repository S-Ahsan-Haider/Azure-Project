from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Cloud Calculator</h1>
        <form method="post">
            <input type="number" name="num1" placeholder="First Number" required>
            <input type="number" name="num2" placeholder="Second Number" required>
            <br><br>
            <button type="submit" formaction="/add">Add (+)</button>
            <button type="submit" formaction="/subtract">Subtract (-)</button>
        </form>
    '''

# Addition

@app.route('/add', methods=['POST'])
def add():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return f"<h2>Addition Result: {n1 + n2}</h2> <br> <a href='/'>Go Back</a>"

# Subtraction

@app.route('/subtract', methods=['POST'])
def subtract():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return f"<h2>Subtraction Result: {n1 - n2}</h2> <br> <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run()