import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('diabet.csv')
df_binary= pd.read_csv('diabbet.csv')
df_dibates = pd.read_csv('diabetes.csv')
df_file = pd.DataFrame(df)
a = df.drop('Diabetes_012' , axis= 1)
b = df ['Diabetes_012']
x_train , x_test , y_train , y_test = train_test_split(a, b , test_size=0.33 , stratify =b, random_state= 0)

smote = SMOTE(random_state = 0)
x_train_sm , y_train_sm = smote.fit_resample(x_train , y_train) 

print(x_train.shape)
print(y_train.shape)

df_binary['age'] = df



print(df_binary['Diabetes_binary'].value_counts())


