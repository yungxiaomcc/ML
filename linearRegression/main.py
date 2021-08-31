# 直接测试环境
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

boston = load_boston()

#print(boston.get("DESCR"))
#print(boston.get('data'))
#print(boston.get('target'))
#print(boston.get('feature_names'))
#print(boston.get('filename'))

x = boston.get('data')
y = boston.get('target')

# 拆分数据集
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=33,test_size=0.25)

ss_x = StandardScaler()
ss_y = StandardScaler()

# 训练与测试数据标准化处理
x_train = ss_x.fit_transform(x_train)
x_test = ss_x.transform(x_test)

y_train = ss_y.fit_transform(y_train)
y_test = ss_y.transform(y_test)

# 使用简单的线性模型预测
lr = LinearRegression()
lr.fit(x_train,y_train)

# 使用测试集得到的测试结果
lr_y_predict = lr.predict(x_test)
print('----------------------')
print(lr_y_predict)

# 使用梯度下降模型预测
from sklearn.linear_model import SGDRegressor
sgdr = SGDRegressor()
sgdr.fit(x_train,y_train)
sgdr_y_predict = sgdr.predict(x_test)
print('----------------------')
print(sgdr_y_predict)

