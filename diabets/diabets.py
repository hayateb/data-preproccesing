import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler , MinMaxScaler


def load_data():
    df = pd.read_csv('diabet.csv')
    df_binary = pd.read_csv('diabbet.csv')
    df_dibates = pd.read_csv('diabets.csv')
    return df , df_binary, df_dibates

def clean_data(df):
      
      if "BMI" in df.columns:
            scaler = StandardScaler()
            df['BMI'] = scaler.fit_transform(df[['BMI']])
            return df
      
def split_data(df, target_coloumn):  
      
      target_coloumn = df.columns[0]  
      a = df.drop(columns=[target_coloumn])
      b= df[target_coloumn]
      x_train, x_test, y_train, y_test = train_test_split(a, b ,test_size=0.2, stratify=b, random_state=0)
      smote = SMOTE(random_state=0)
      x_train_sm, y_train_sm = smote.fit_resample(x_train, y_train)     
      return x_train_sm, y_train_sm, 



df, df_binary, df_dibates = load_data()
df = clean_data(df)
df_binary = clean_data(df_binary)
df_dibates = clean_data(df_dibates)

# Example: using df and assuming the target column is the first column
x_train_sm ,y_train_sm,  = split_data(df, df.columns[0])
x_train_sm , y_train_sm = split_data(df_binary, df_binary.columns[0])

print(df_binary)
# print(df_binary)
# print(df_dibates)
print(y_train_sm.value_counts())
print(y_train_sm.value_counts()) 

