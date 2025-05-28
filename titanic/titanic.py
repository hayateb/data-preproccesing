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

df_train = pd.read_csv('train.csv')
df_file = pd.read_csv('test.csv')
df = pd.DataFrame(df_train)
df_test =pd.DataFrame(df_file)

# first cleaning the data by convert to lowercase 

df['Name'] = df['Name'].str.lower()
df_test['Name'] = df_test['Name'].str.lower()
 
# remove the special characters from the name column

df['Name'] = df['Name'].str.replace(r'[^a-z\s]', '', regex=True)
df_test['Name'] = df_test['Name'].str.replace(r'[^a-z\s]', '', regex=True)

# as this dataset in age cooumn there are missing value so for numerical value we
# we use filling them with mean method  fro both files 
df['Age'] = df['Age'].fillna(df['Age'].mean())
df_test['Age'] = df_test['Age'].fillna(df_test['Age'].mean())

# for missing more thatn 50 percent we remove the coloumn at all 
threshold = 0.5 * len(df)
df = df.dropna(thresh=threshold, axis = 1)

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

# after all the cleaning 


# ecoding with manual label coding 
df['Sex'] = df['Sex'].map({"female": 1, "male": 0})
df_test['Sex'] = df_test['Sex'].map({"female": 1, "male": 0})
print( df)
print(df_test)

