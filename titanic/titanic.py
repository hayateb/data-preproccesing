import pandas as pd
import numpy as np

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
df = pd.DataFrame(df_train)
df_test =pd.DataFrame(df_test)


df['Age'] = df['Age'].fillna(df['Age'].mean())
threshold = 0.5 * len(df_test)
df_test = df.dropna(thresh=threshold, axis = 1)


print(df['Age'].isnull().sum())
print(df_test)

