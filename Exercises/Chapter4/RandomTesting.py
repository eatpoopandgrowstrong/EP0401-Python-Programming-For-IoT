import matplotlib.pyplot as plt
import numpy as np

line_1 = np.random.randint(low = 0, high = 50, size = 50)
line_2 = np.random.randint(low = -15, high = 100, size = 50)

fig, ax = plt.subplots()

ax.plot(line_1, color = 'green', label = 'Line 1')
ax.plot(line_2, color = 'red', label = 'Line 2')
ax.legend(loc = 'upper left')
plt.show()