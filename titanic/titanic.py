# the neccesary data cleaning specificed for this dataset are
# 1. convert the names to lower case and remove special characters for text in name column
# 2. fill the missing values in the age column with mean which the missing values are not more than 50 percent
# 3. remove the columns which have more than 50 percent missing values cabin coloumn
# 4. for the catagorical sex coloumn encoding with numerical values for the algthiritm gender submission 
#
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler , MinMaxScaler  , LabelEncoder

# load the dataset and reading as csv file and cahnge to dataframe
def load_data():
    # Load the training and test datasets
    df_train = pd.read_csv('train.csv')
    df_test = pd.read_csv('test.csv')
    return df_train, df_test
# cleaning the data
def clean_data(df):
      df['Name'] = df['Name'].str.lower() # convert names to lower case
      df['Name'] = df['Name'].str.replace(r'[^a-z\s]', '', regex=True) # remove special characters
      df['Age'] = df['Age'].fillna(df['Age'].median()) # fill missing values in Age with mean
      threshold = 0.5 * len(df)
      df = df.dropna(thresh=threshold, axis = 1)
      encode = LabelEncoder()
      df['Sex'] = encode.fit_transform(df['Sex'])
      return df


df_train, df_test = load_data()
df = pd.DataFrame(df_train)
df_test = pd.DataFrame(df_test)

df = clean_data(df)
df_test = clean_data(df_test)

colomns = df.columns.intersection(df_test.columns)
df_test = df_test[colomns]
# checking the missing value in both files
print(" the missing value of train dta"  , df.columns.isnull().sum())
print("the missing value for test file",df_test.columns.isnull().sum())

# print("hjjh", df)
# q1 = df['Age'].quantile(0.25)
# q3 = df['Age'].quantile(0.75)
# iqr = q3 - q1
# outliner = (df['Age'] < (q1 - 1.5 * iqr)) | (df['Age'] > (q3 + 1.5 * iqr))
# # -6  , 66
# df = df[~outliner]
print(df)


