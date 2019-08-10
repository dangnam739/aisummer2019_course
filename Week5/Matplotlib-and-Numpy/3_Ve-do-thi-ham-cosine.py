import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-10, 10, 0.01)
y = np.cos(x)
plt.title('Cosine Function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x, y)
plt.show()
