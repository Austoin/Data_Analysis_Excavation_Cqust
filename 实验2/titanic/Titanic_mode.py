import pandas as pd

#数据加载
df=pd.read_csv('train.csv')


print(df.describe())#查看数据的大体情况


#使用众数填充
df['Age']=df['Age'].fillna(df['Age'].mode()[0])


#使用拉格朗日插值法填充
from scipy.interpolate import lagrange

#自定义插值函数
#s为列向量，n插值位置，k为取前后数据个数，默认为5
def ployinterp_column(s,n,k=5):
    y=s.reindex(list(range(n-k,n))+list(range(n+1,n+1+k)))#取前后k个数
    y=y[y.notnull()] #删除空值
    return lagrange(y.index,list(y))(n) #插值并返回结果
#逐个元素判断是否需要插值
for i in range(len(df['Age'])):
    if (df['Age'].isnull())[i]:
        df['Age'][i]=ployinterp_column(df['Age'],j)

print(df['Age'].count()) #统计Age列中非空元素个数




