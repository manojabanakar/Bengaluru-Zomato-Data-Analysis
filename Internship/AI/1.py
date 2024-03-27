import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('Debernardi et al 2020 data.csv')
#print(data)



feature_cols=['age','sex','plasma_CA19_9','creatinine','LYVE1','REG1B','TFF1','REG1A']
x=data[feature_cols]
#print(x)

y=data.diagnosis
#print(y)

data.drop(columns=['sample_id','patient_cohort','sample_origin','stage','benign_sample_diagnosis'],axis=1,inplace=True)
#print(data)

L=len(y)
for i in range(L):
    if y[i]==3:
        y[i]=1
    else:
        y[i]=0


for i in data[2:]:
    if i!='sex':
        data[i]=data[i].fillna(data[i].mean())
#print(data)

sex=pd.get_dummies(data['sex'],drop_first=True)
#print(sex)
X=pd.concat([data,sex],axis=1)
print(X)

from sklearn.model_selection import train_test_split
x_train, y_train, x_test, y_test=train_test_split(x,y,test_size=0.20, random_state=2)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
pred=logreg.predict(x_test)
#print(pred)








