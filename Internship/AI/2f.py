import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('C:/Users/User/Desktop/Project/Debernardi et al 2020 data.csv')
#print(dataset)

y=dataset.diagnosis
x=dataset.drop(columns=['sample_id','patient_cohort','sample_origin','diagnosis','stage','benign_sample_diagnosis'])
#print(x)
L=len(y)
for i in range(L):
    if y[i]==3:
        y[i]=1
    else:
        y[i]=0

for i in x[2:]:
    if i!='sex':
        x[i] = x[i].fillna(x[i].mean())
#print(x)

x=pd.get_dummies(x)
#print(x)

from sklearn import svm
from sklearn.model_selection import train_test_split

clf = svm.SVC()

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=50)

SVM = clf.fit(X_train, y_train)

score = SVM.score(X_test, y_test)
print('Test set score: {}'.format(score))

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)

y_pred=reg.predict(X_test)
y_pred1=reg.predict([[10,1,0,1.700000,1.83222,0.89321,20.9486,150.282,1262.000000]])
#print(y_pred1)



plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, reg.predict(X_train), color='blue')
plt.title('Salary VS Experience (Training set)')
plt.xlabel('Year of Experience')
plt.ylabel('Salary')
plt.show()
'''
from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
pred=logreg.predict(X_test)
print(pred)
#y_pred1=regressor_predict([[]])
#print(y_pred1)
'''
