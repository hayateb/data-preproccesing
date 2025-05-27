import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Housing.csv')

df_house = pd.DataFrame(df)

df_ecoded = pd.get_dummies(df_house , columns=['furnishingstatus'])



print(df_ecoded)