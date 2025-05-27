import pandas as pd
import numpy as np
import seaborn as sns
from  sklearn.preprocessing import LabelEncoder

df = sns.load_dataset('iris', cache = True , data_home = None )

df_clean = pd.get_dummies(df, columns= ['species'])

print(df_clean)