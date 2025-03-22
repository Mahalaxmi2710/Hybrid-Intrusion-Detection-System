import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

#Here it aims at finding malicious files that can be detected and sent to the virtual sandbox for futher details

#Load Data
train_df = pd.read_csv("UNSW_NB15_training-set.csv") # training set of UNSW_NB15 from kaggle
test_df = pd.read_csv("UNSW_NB15_testing-set.csv") # test set of UNSW_NB15 from kaggle

# Selecting relevant features
selected_features = ['sbytes', 'dbytes', 'dur', 'sinpkt', 'dttl', 'tcprtt', 'ct_srv_src', 'ct_srv_dst']
X_train = train_df[selected_features]
y_train = train_df['label']
X_test = test_df[selected_features]
y_test = test_df['label']

# Train Random Forest model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)

# Model Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
