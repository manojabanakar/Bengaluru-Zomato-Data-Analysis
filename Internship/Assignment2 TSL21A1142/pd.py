from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
data=pd.read_csv ("DailyActivity.csv")
x=data['TotalSteps']
y=data['Calories']
plt.title('DailyActivity')
plt.xlabel('TotalSteps')
plt.ylabel('Calories')
plt.bar(x,color='r',label="TotalSteps",height=0.5)
plt.bar(y,color='y',label="Calories",height=0.5)
plt.legend()
plt.show()
