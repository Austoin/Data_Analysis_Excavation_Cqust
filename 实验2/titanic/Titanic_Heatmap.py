import pandas as pd

#数据加载
df=pd.read_csv('train.csv')

#print(df.describe())#查看数据的大体情况

#需安装seaborn库
import seaborn as sns
import matplotlib.pyplot as plt


corrmat=df.corr()#得到相关系数
plt.subplots(figsize=(7,7))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.show



