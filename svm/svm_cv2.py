import cv2
import numpy as np
import matplotlib as plt
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
erray([[155,48],[159,50],[164,53],[164,56],[172,60]])
rand2 = np.array([[152,53],[156,55],[160,56],[172,64],[176,65]])
 
#lable
lable = np.array([0],[0],[0],[0],[0],[1],[1],[1],[1],[1])
 
#data 处理
data = np.vstack(rank1,rand2)
data = np.array(data,dtype='float32')
 
#所有的数据必须一一对应的lable
#监督学习 0负样本1正样本
 
#训练
svm = cv2.ml.SVM_create() #创建SVM model
#属性设置
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)
#训练
result = svm.train(data,cv2.ml.ROW_SAMPLE,lable)
#预测
 
pt_data = np.vstack([[167,55],[162,57]])
pt_data = np.array(pt_data,dtype='float32')
print(pt_data)
(par1,par2) = svm.predict(pt_data)
print(par2)

