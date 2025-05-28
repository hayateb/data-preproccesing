# use the standard scaler to scale the iris dataset
# and catagory the species column with numerical values
import pandas as pd
import numpy as np
import seaborn as sns
from  sklearn.preprocessing import LabelEncoder ,StandardScaler

df = sns.load_dataset('iris', cache = True , data_home = None )


encoder = LabelEncoder()

df['species'] = encoder.fit_transform(df['species'])
cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for col in cols:
      scale = StandardScaler()
      df[col] = scale.fit_transform(df[[col]])
print(df)