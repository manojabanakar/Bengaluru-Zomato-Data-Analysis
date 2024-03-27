from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import style
data=pd.read_csv("DailyActivity.csv")
Calories=data['Calories']
Calories_range=[1000,1250,1500,1750,2000,2250,2500,2750,3000]
plt.hist(Calories,Calories_range,histtype='bar',rwidth=0.6)
plt.xlabel("Calories")
plt.ylabel("TotalSteps")
plt.title("Histogram")
plt.show()
