from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <body style="font-family: sans-serif; text-align: center; background-color: #f4f4f4;">
            <div style="margin-top: 50px; background: white; display: inline-block; padding: 20px; border-radius: 10px; shadow: 0px 4px 6px rgba(0,0,0,0.1);">
                <h1>☁️ Cloud Calculator</h1>
                <form method="post">
                    <input type="number" name="num1" placeholder="First Number" style="padding: 10px;" required>
                    <input type="number" name="num2" placeholder="Second Number" style="padding: 10px;" required>
                    <br><br>
                    <button type="submit" formaction="/add" style="background: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Add (+)</button>
                    <button type="submit" formaction="/subtract" style="background: #dc3545; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Subtract (-)</button>
                </form>
            </div>
        </body>
    '''

# Addition

@app.route('/add', methods=['POST'])
def add():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return f"<h2>Result: {n1} + {n2} = {n1 + n2}</h2> <br> <a href='/'>Go Back</a>"

# Subtraction

@app.route('/subtract', methods=['POST'])
def subtract():
    n1 = int(request.form['num1'])
    n2 = int(request.form['num2'])
    return f"<h2>Result: {n1} - {n2} = {n1 - n2}</h2> <br> <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run()