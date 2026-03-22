from flask import Flask, request

app = Flask(__name__)

# Home page of my calculator

@app.route('/')
def home():
    return '''
        <h1>Cloud Calculator</h1>
        <form action="/add" method="post">
            <input type="number" name="num1" placeholder="First Number" required> +
            <input type="number" name="num2" placeholder="Second Number" required>
            <button type="submit">Calculate</button>
        </form>
    '''

# Calclation part

@app.route('/add', methods=['POST'])
def add():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return f"<h2>The Result is: {n1 + n2}</h2> <br> <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run()
