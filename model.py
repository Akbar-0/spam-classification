import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Download stopwords
nltk.download('stopwords')

# Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv")[['id', 'label', 'tweet']]

# Drop missing values in label column
df = df.dropna(subset=['label'])

# Ensure labels are numeric (if needed)
df['label'] = df['label'].astype(int)

# Display class distribution
print(df['label'].value_counts())

# Text preprocessing
stop_words = set(stopwords.words('english'))
df['tweet'] = df['tweet'].apply(
    lambda text: " ".join([word.lower() for word in text.split() if word.lower() not in stop_words])
)

# Convert text to numerical features
vectorizer = TfidfVectorizer(max_features=2000)
X = vectorizer.fit_transform(df['tweet'])
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model (Naïve Bayes)
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Print detailed classification report
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

# Save Model & Vectorizer
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
