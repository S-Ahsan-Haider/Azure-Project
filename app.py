from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Loading model (only once at startup)
with open('iris_model.pkl', 'rb') as f:
    moda = pickle.load(f)

@app.route('/')
def home():
    return "<h1>Iris Species Predictor</h1><p>Send a POST request to /predict with JSON data.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    # Expecting JSON: {"data": [5.1, 3.5, 1.4, 0.2]}
    data = request.get_json(force=True)
    prediction = moda.predict([np.array(data['data'])])

    # No. back to flower name
    target_names = ['setosa', 'vesicolor', 'virginica']
    result = target_names[prediction[0]]

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run()