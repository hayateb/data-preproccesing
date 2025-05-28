# the preproccesing i used for this cleaning are catagorical encoding using banary encoding
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder 


df = pd.read_csv('Housing.csv')
df_house = pd.DataFrame(df)

for col in ['mainroad', 'prefarea', 'furnishingstatus']:
    encoder = LabelEncoder()  # or your encoder
    df_house[col] = encoder.fit_transform(df_house[col])

print(df_house)
