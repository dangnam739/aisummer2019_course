import matplotlib.pyplot as plt
import numpy as np

def relu_function(data):
    return (np.abs(data) + data) / 2

def relu_derivate(data):
    return (data > 0) * 1

data = np.arange(-2., 2., 0.01)
data_relu = relu_function(data)
data_drelu = relu_derivate(data)

fig, ax = plt.subplots(figsize=(10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Creat and show plot
ax.plot(data, data_relu, color='#d35400', linewidth=3, label='ReLU')
ax.plot(data, data_drelu, color='#1abd15', linewidth=3, label='derivative')
ax.legend(loc='upper left', frameon=False)
fig.show()
