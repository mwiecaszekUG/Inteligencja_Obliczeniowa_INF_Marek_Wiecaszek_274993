import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

dataset = pd.read_csv("iris.csv")

X = dataset[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']].apply(
    lambda x: (x - x.min()) / (x.max() - x.min()))
y = dataset[['class']].replace(["setosa", "versicolor", "virginica"], [0, 1, 2])

df = pd.concat([X, y], axis=1)

train, test = train_test_split(df, test_size=0.3, random_state=274993)

trainX = train[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']]
trainY = train['class']
testX = test[['sepallength', 'sepalwidth', 'petallength', 'petalwidth']]
testY = test['class']
# print(trainX.head(5))
# print(testY.head(5))

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(4, 2, 1), random_state=1)

clf.fit(trainX, trainY)

prediction = clf.predict(testX)
print("Prawdziwe wyniki: ", testY.values)
print("Wyniki z sieci 4-2-1", prediction)
print('Skuteczność 4-2-1:', sklearn.metrics.accuracy_score(prediction, testY))

# Prawdopodobnie wyniki 0<0.33<0.66<1 są zamieniane na 0, 1 i 2 w zależności od przefdziału.

clf2 = MLPClassifier(hidden_layer_sizes=(4, 3, 1), random_state=1)

clf2.fit(trainX, trainY)

prediction2 = clf2.predict(testX)

print('Skuteczność 4-3-1:', sklearn.metrics.accuracy_score(prediction2, testY))

clf3 = MLPClassifier(hidden_layer_sizes=(4, 3, 3, 1), random_state=1)

clf3.fit(trainX, trainY)

prediction3 = clf3.predict(testX)

print('Skuteczność 4-3-3-1:', sklearn.metrics.accuracy_score(prediction3, testY))

clf4 = MLPClassifier(hidden_layer_sizes=(4, 3, 3), random_state=1)

clf4.fit(trainX, trainY)

prediction4 = clf4.predict(testX)

print('Skuteczność 4-3-3:', sklearn.metrics.accuracy_score(prediction4, testY))




