from load_data import load_data
from sort import bubble_sort
from matplotlib import pyplot as plt
import numpy as np

time_data = load_data('activity.csv')
time = np.cumsum(time_data['Duration'])

print(time)

data = load_data('activity.csv')
power_W = data['PowerOriginal']
print(power_W)
sorted_power_W = bubble_sort(power_W)
print(sorted_power_W[::-1])

plt.plot(time/60, sorted_power_W[::-1],color='green', linewidth=2)
plt.xlabel('Time (min)')
plt.ylabel('Power (W)')
plt.title('Power Curve')
plt.grid(True)
plt.xticks()
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.savefig('power_curve.png')
plt.show()
plt.close()

