from matplotlib import pyplot as plt
activities=['sleep','eat','work','games']
duration=[7,2,13,2]
colors=['r','g','b','y']
plt.pie(duration,label="activities",colors=colors,shadow=True,autopet="%1.1f%%")
plt.title("My activities")
plt.show()
