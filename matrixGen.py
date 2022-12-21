import random


numCubes = 2
numLayers = 3
numX = 3
numY = 16

count = 0

arrCube = []
for cubes in range(numCubes):
    arrLayer = []
    for layer in range(numLayers):
        arrX = []
        for x in range(numX):
            arrY = []
            for y in range(numY):
                
                num = (random.randint(0, 255)) - 128

                test = (random.randint(0, 99)) + 1

                if (test <= 80):
                    num = 0
                    count += 1

                arrY.append(num)

            arrX.append(arrY)

        arrLayer.append(arrX)

    arrCube.append(arrLayer)


print (arrCube)

print ((100 * count)/(numCubes * numLayers * numX * numY))

print ('\n')
                


