import pandas as pd

#数据加载
df=pd.read_csv('train.csv')


print(df.describe())#查看数据的大体情况

#针对Age列进行数据规范化
import numpy as np
Age=df['Age']

n1=(Age-Age.min())/(Age.max()-Age.min())#最小-最大规范化
n2=(Age-Age.mean())/Age.std() #零-均值规范化
n3=Age/10**np.ceil(np.log10(Age.abs().max()))#小数定标规范化
print(n1,n2,n3)



