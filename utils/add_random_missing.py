import pandas as pd
import numpy as np
from random import choice

df = pd.read_csv(r'/media/vlad/STUDY/ETU/7 семестр/МашОбуч/code/data/Bank_Customer_Churn_Prediction.csv')
random_rows = np.random.randint(0, df.shape[0] + 1, size = (df.shape[0]*2)//100)
for row in random_rows:
    df.loc[row, [choice(df.columns)]] = np.nan

df.to_csv('data/bank_data.csv', index=False)