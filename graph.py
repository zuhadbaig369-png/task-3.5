import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
savings = [70, 85, 60, 90, 75]

plt.plot(days, savings)
plt.title('My savings tracker')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 180)
plt.show()
plt.plot(days, savings, marker='o', linestyle='dotted', color='red', linewidth=2)
plt.title('My savings tracker')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 180)
plt.show()
plt.bar(days, savings, color='green')
plt.title('My savings tracker')
plt.xlabel('Days of the week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 180)
plt.show()