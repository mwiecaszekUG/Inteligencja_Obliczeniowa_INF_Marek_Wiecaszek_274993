import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix

df = pd.read_csv("diabetes.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=1337)

print(test_set)
print(train_set)

train_inputs = train_set[:, 0:8]
train_classes = train_set[:, 8]
test_inputs = test_set[:, 0:8]
test_classes = test_set[:, 8]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_inputs, train_classes)

plot_confusion_matrix(clf, test_inputs, test_classes)

plt.show()

tree.plot_tree(clf)
plt.show()

result = clf.score(test_inputs, test_classes)

print(result)