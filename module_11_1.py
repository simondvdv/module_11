import random
import numpy

data_list = numpy.random.randint(-100, 100, (5, 3))
data_list_2 = numpy.random.randint(-100, 100, (3, 2))
print(data_list)
print(data_list.ndim)
print(data_list.shape)
print(data_list.size)
print(data_list.sum())
print(data_list.min())
print(numpy.dot(data_list, data_list_2))
