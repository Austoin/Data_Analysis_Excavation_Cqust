import pandas as pd

df=pd.read_csv('train.csv')
a=df.head(5)
b=df.tail(5)
c=df.columns
d=df.info()
e=df.describe()

total=df.isnull().sum().sort_values(ascending=True)