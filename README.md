# 📧 Spam Classifier

A simple **Spam Classifier** using **Naive Bayes & TF-IDF**, built with Python & Flask.

## 🚀 Setup & Run
```sh
# Clone the repo
git clone https://github.com/Akbar-0/spam-classifier.git
cd spam-classifier

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
    "message": "Win a free iPhone now!"
}
```
Response:
```json
{
    "spam": true
}
```
