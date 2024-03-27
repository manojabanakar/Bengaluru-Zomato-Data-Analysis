from matplotlib import pyplot as plt
plt.bar([1,2,3,4,5],[50,33,54,67,84],label="BMW",width=0.4,color='r')
plt.bar([1,2,3,4,5],[23,24,46,25,75],label="AUDI",width=0.2,color='y')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Cars Sold")
plt.title("Car sales data")
plt.show()
