import pandas as pd

#数据加载
df=pd.read_csv('train.csv')

#粗略统计
df.head(5)  #显示前5行数据
df.tail(5)#显示后5行数据
df.columns #查看列名
df.info()#查看各个段的信息
df.shape #查看数据集行列分布（几行几列）
df.describe()#查看数据的大体情况

#处理缺失值
#统计缺失值数量
total=df.isnull().sum().sort_values(ascending=False)
print(total)

#缺失值处理
#填充值
#使用中位数填充
df['Fare']=df['Fare'].fillna(df['Fare'].median())

#使用平均数填充
df['Age']=df['Age'].fillna(df['Age'].mean())

#删除缺失值

#删除空值列
df=df.drop(['Cabin'],axis=1)

#删除空值行
df_new=df.drop(df[df['Embarked'].isnull()].index)


#查找重复值
df.duplicated()

#删除重复行（保留1项）
df.drop_duplicates()

#删除重复行（保留0项）
df.drop_duplicates(keep=False)

#查找异常值(describe方法）
df.describe()

#查找异常值(箱型图)

# 将异常值替换为平均值
df.replace([512.329200],df['Fare'].mean())

#统计乘客死亡和存活人数
df['Survived'].value_counts()


#统计乘客中男女性别人数
df['sex'].value_counts()

#统计男女获救人数
survive = df['sex'][df['survived']==1].value_counts()

#使用corr()函数判断属性间相关性
df['pclass'].corr(df['survived'])

#绘制乘客票价与舱位等级箱型图Boxplot
df.boxplot(['fare'],['pclass'])

#保存预处理后数据集
df.to_json('titanic_after_preprocessing.json') #保存到json文件
df.to_csv('titanic_after_preprocessing.csv') #保存到csv文件
df.to_excel('titanic_after_preprocessing.xls')#保存到excel文件






