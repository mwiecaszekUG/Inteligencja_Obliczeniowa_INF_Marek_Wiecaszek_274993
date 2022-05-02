import pandas as pd
import numpy as np

missing_values = ["n/a", "NA", "-", "Versicolour"]
df = pd.read_csv("iris_with_errors.csv", na_values=missing_values)

print("Przed naprawieniem")
print(df.isnull().sum())
print(df.describe(include='all'))

df['variety'] = df['variety'].str.upper()
df['variety'].fillna("VERSICOLOR", inplace=True)
median = df['sepal.length'].median()
df['sepal.length'].fillna(median, inplace=True)
median = df['sepal.width'].median()
df['sepal.width'].fillna(median, inplace=True)
median = df['petal.width'].median()
df['petal.width'].fillna(median, inplace=True)
median = df['petal.length'].median()
df['petal.length'].fillna(median, inplace=True)


def rm_bad_numbers(column_name):
    median_func = df[column_name].median()
    df[column_name] = df[column_name].apply(lambda x: x if 0 < x < 15 else median_func)


rm_bad_numbers("sepal.length")
rm_bad_numbers("sepal.width")
rm_bad_numbers("petal.width")
rm_bad_numbers("petal.length")

print("Po naprawieniu")
print(df.isnull().sum())
print(df.describe(include='all'))

df.to_csv("naprawione.csv", index=False)
