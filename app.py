from flask import Flask, request, render_template_string
import pickle
import numpy as np

app = Flask(__name__)

# Loading model (only once at startup)
with open('iris_model.pkl', 'rb') as f:
    moda = pickle.load(f)

# Simple CSS-styled HTML for a clean mobile look
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Iris Predictor</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: sans-serif; text-align: center; background-color: #f0f2f5; padding: 20px; }
        .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; margin: auto; }
        input { width: 80%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; }
        button { background-color: #0078d4; color: white; border: none; padding: 12px 20px; border-radius: 5px; cursor: pointer; width: 85%; font-size: 16px; }
        .result { margin-top: 20px; font-weight: bold; color: #0078d4; font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🌸 Iris Species Predictor</h2>
        <form action="/predict" method="post">
            <input type="number" step="0.1" name="s_length" placeholder="Sepal Length (cm)" required>
            <input type="number" step="0.1" name="s_width" placeholder="Sepal Width (cm)" required>
            <input type="number" step="0.1" name="p_length" placeholder="Petal Length (cm)" required>
            <input type="number" step="0.1" name="p_width" placeholder="Petal Width (cm)" required>
            <button type="submit">Predict Species</button>
        </form>
        {% if prediction %}
            <div class="result">Prediction: {{ prediction }}</div>
            <a href="/">Try another</a>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return "<h1>Iris Species Predictor</h1><p>Send a POST request to /predict with JSON data.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    # Taking Values from the form
    features = [
        float(request.form['s_length']),
        float(request.form['s_width']),
        float(request.form['p_length']),
        float(request.form['p_width']),
    ]

    # No. back to flower name
    prediction = moda.predict([np.array(features)])
    target_names = ['Setosa', 'Vesicolor', 'Virginica']
    result = target_names[prediction[0]]

    return render_template_string(HTML_TEMPLATE, prediction=result)

if __name__ == '__main__':
    app.run()