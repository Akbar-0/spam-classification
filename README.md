# 📧 Spam Classifier

A simple **Spam Classifier** using **Naive Bayes & TF-IDF**, built with Python & Flask.

## 🚀 Setup & Run
```sh
# Clone the repo
git clone https://github.com/Akbar-0/spam-classifiction.git
cd spam-classifiction

# Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run the API
python app.py
```

## 📡 API Usage
Send a  request to  with:
```json
{
    curl -X POST http://YOUR.IP.ADDRESS.HERE:8000/predict -H "Content-Type: application/json" -d "{\"message\": \"There you have it folx. The numbers don't lie. Americans are mostly...\"}"
}
```
Response:
```json
{
    "spam": true
}
```
