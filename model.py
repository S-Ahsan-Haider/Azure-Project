import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Data Loading
iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train model
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=1)
moda = RandomForestClassifier()
moda.fit(xtrain, ytrain)

# Saving model
with open('iris_model.pkl', 'wb') as f:
    pickle.dump(moda, f)

print("model saved!")

