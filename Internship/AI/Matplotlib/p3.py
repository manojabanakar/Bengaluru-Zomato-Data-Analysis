from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd

data=pd.read_csv('diabetes.csv')
x=data ['BMI']
y=data [ 'Outcome']

plt.scatter(x,y)
plt.show()
