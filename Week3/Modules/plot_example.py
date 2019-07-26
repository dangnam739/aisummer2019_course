import matplotlib.pyplot as plt
import math
#ham linear space de sinh ra day so tuyen
#tinh trong doan [start, stop] voi so luong
#num cho truoc

def linear_space(start, stop, num=10):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    assert num > 1, 'num should be greater than 1'

    step = (stop - start) / num

    result = []

    for i in range(num):
        result.append(start + step * i)

    return result

#test ham
# result = linear_space(1,8, 7)
# print(result)

def tanh_function(data):
    return [(math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)) for x in data]

#dao ham cua ham tanh
def tanh_derivative(data):
    return [1 - x**2 for x in data]

# calculate plot point
data = linear_space(-5., 5., 100)
data_tanh = tanh_function(data)
data_dtanh = tanh_derivative(data)

#crate and show plot function tanh
# plt.plot(data, data_tanh, color='#d35400', linewidth=3)
# plt.show()

#chinh lai 4 truc
fig, ax = plt.subplot(figsize=(10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#tao va hien thi bieu do
ax.plot(data, data_tanh, color='#d35400', linewidth=3, label='tanh')
ax.plot(data, data_dtanh, color='#1abd15', linewidth=3, label='derivative')
ax.legend(loc='upper left', frameon=False)
fig.show()
