import pandas as pd

#数据加载
df=pd.read_csv('train.csv')


print(df.describe())#查看数据的大体情况


#查找异常值(箱型图方法), 建议用spyder观测数据结构
import matplotlib.pyplot as plt
plt.figure()
p=df.boxplot(return_type='dict')#绘制箱型图
x=p['fliers'][6].get_xdata()#fliers为异常值标签
y=p['fliers'][6].get_ydata()#x为x轴数据，y为y轴数据
plt.show()






