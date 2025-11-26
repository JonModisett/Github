import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a function to create a simple neural network model
def create_model():
    model = Sequential()
    model.add(Dense(8, input_dim=4, activation='relu'))
    model.add(Dense(3, activation='softmax'))  # 3 classes for the 3 Iris species
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Create a Scikit-learn pipeline that uses a Keras neural network and a Scikit-learn Random Forest
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Standardization
    ('nn', KerasClassifier(build_fn=create_model, epochs=100, verbose=0)),  # Neural network
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))  # Random forest
])

# Fit the pipeline
pipeline.fit(X_train, y_train)

# Predict and evaluate on the test data
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
