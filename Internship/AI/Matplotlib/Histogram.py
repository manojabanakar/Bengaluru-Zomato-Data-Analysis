from matplotlib import pyplot as plt
population=[20,22,26,35,65,78,52,44,12,63,78,11,46,82,16,35,96,74,35]
age_range=[0,10,20,30,40,50,60,70,100]
plt.hist(population,age_range,histtype='bar',rwidth=0.8)
plt.xlabel("Age group")
plt.ylabel("No of People")
plt.title("Histogram")
plt.show()
