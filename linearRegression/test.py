import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os
path = 'data' + os.sep + 'LogiReg_data.txt'
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
# print(pdData.head())
# print(pdData.shape)

# 返回 满足条件的指定列
positive = pdData[pdData['Admitted'] == 1] 
negative = pdData[pdData['Admitted'] == 0] 

# print('-----------positive-------')
# print(positive)
# print('-----------negtive-----')
# print(negative)

fig,ax=plt.subplots(figsize=(10,5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')




pdData.insert(0, 'Ones', 1)
# print('------------')
# print(pdData)
# print(hasattr(pdData,"as_matrix"))
# pdData :pandas.core.frame.DataFrame
print(type(pdData))



cols = pdData.shape[1]
# print(cols)
# print(pdData[:,0:cols-1])
# print(pdData[:,cols-1:cols])