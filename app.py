from flask import Flask, request, jsonify
import pickle

# Load trained model & vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['message']
    print(f"\n🔹 Received Message: {data}")  # Debugging
    message_vector = vectorizer.transform([data])
    prediction = model.predict(message_vector)[0]
    print(f"🔹 Potential Spam: {bool(prediction)}")  # Debugging
    return jsonify({'spam': bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
