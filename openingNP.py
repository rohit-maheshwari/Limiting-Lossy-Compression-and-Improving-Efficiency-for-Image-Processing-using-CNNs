import numpy as np

# data = np.random.normal(0, 1, 100)
# np.save('tensor.npy', data)

arrCube = np.load('tensor16.npy')

shape = arrCube.shape



print(arrCube.shape)

arrCube = np.rollaxis(arrCube, 3, 1)

print(arrCube)

print(arrCube.shape)

arrCube = arrCube.tolist()
# print(arrCube)