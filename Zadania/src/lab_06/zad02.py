import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")

print(df.describe(include='all'))

features = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth']
# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:, ['class']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents
                           , columns=['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['class']]], axis=1)
print(finalDf.describe(include='all'))


def sum_col(lower, upper, col_list):
    result = 0
    while lower <= upper:
        print(lower)
        result += df[col_list[lower]].var()
        lower += 1
    return result


strata_dla_2 = 1 - (sum_col(2, 3, features) / sum_col(0, 3, features))
strata_dla_1 = 1 - (sum_col(1, 3, features) / sum_col(0, 3, features))
strata_dla_3 = 1 - (sum_col(3, 3, features) / sum_col(0, 3, features))
print("strata dla 1: ", strata_dla_1)
print("Strata dla 2: ", strata_dla_2)
print("strata dla 3: ", strata_dla_3)

# strata informacji dla jednej usuniętej kolumny to ok. 15% dla 2 ok.19%,
# a dla 3 to już ok.87% dlatego usuwamy 2 kolumny

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['setosa', 'versicolor', 'virginica']
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['class'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c=color
               , s=50)
ax.legend(targets)
ax.grid()
plt.show()
