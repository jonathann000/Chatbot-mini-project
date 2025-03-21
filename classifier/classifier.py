import random
import numpy as np
from langchain_nomic.embeddings import NomicEmbeddings
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from questions import restaurant_questions, transport_questions, weather_questions, train_x, train_y, test_x, test_y

# Initialize embedding model
embedding_model = NomicEmbeddings(model="nomic-embed-text-v1.5", inference_mode="local")

# Embed training questions
train_embeddings = np.array([embedding_model.embed_query(q) for q in train_x])

# Train a classifier (Logistic Regression with Standardization)
classifier = make_pipeline(StandardScaler(), LogisticRegression())
classifier.fit(train_embeddings, train_y)

# Test classification
test_embeddings = np.array([embedding_model.embed_query(q) for q in test_x])
predictions = classifier.predict(test_embeddings)

# Evaluate accuracy
accuracy = sum(p == t for p, t in zip(predictions, test_y)) / len(test_y)
print(f"Classification Accuracy: {accuracy:.2%}")

# Sample predictions
for q, pred in zip(test_x[:5], predictions[:5]):
    print(f"Q: {q} → Predicted: {pred}")

import joblib

# Save the trained classifier (including scaler and embedding model)
joblib.dump(classifier, 'trained_classifier_model_new.pkl')

print("Model saved to 'trained_classifier_model_new.pkl'") 
