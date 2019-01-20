import pandas as pd

# filtering the data
header = ["BI_RADS", "age", "shape", "margin", "density", "severity"]
df = pd.read_csv("csv/mammographic_masses.csv", names=header, usecols=range(6), na_values='?')
df.dropna(inplace=True)

# dividing the labels abd features
labels = df['severity'].values
features = df[['BI_RADS', 'age', 'shape', 'margin', 'density']].values

# scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
print(scaled_features)
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(scaled_features, labels, test_size=0.25,
                                                                            random_state=1)
# Decision Tree
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=15)
clf = clf.fit(features_train, labels_train)

# confusion matrix
print('Accuracy is ', clf.score(features_test, labels_test))
