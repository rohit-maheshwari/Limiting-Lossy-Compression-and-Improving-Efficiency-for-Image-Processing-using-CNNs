# import numpy as np
import csv
import openingNP


arrCube = openingNP.arrCube

type = openingNP.type
percentThreshold = openingNP.percentThreshold


numCubes = len(arrCube) # 16
numFilters = len(arrCube[0]) # 16
numX = len(arrCube[0][0]) # 3
numY = len(arrCube[0][0][0]) # 3

def checkFilters(arr1, arr2):

    count = 0

    for row in range(numX):
        for col in range(numY):
            if (arr1[row][col] == arr2[row][col]):
                count += 1
    
    percentFilter = (100*count)/(numX * numY)

    return percentFilter

def checkCubes(arr1, arr2):

    count = 0
    
    for filter in range(numFilters):
        percentFilter = checkFilters(arr1[filter], arr2[filter])
        count += (percentFilter*(numX*numY))/100
    
    percentCube = (100*count)/(numFilters*numX*numY)

    return percentCube

def zeroFilterFunction(arr, percent):

    count = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == 0):
                count += 1
    
    percentZero = (100*count)/(numX*numY)
    if (percentZero >= percent):
        return True
    else: 
        return False


def zeroCubeFunction(arr, percent):

    count = 0

    for x in range(len(arr)):
        for i in range(len(arr[x])):
            for j in range(len(arr[x][i])):
                if (arr[x][i][j] == 0):
                    count += 1
                    

    percentZero = (100*count)/(numFilters*numX*numY)
    if (percentZero >= percent):
        return True
    else:
        return False

zeroFilters = 0
cubeMatching = 0
isValidZeros = False

adjListFilters = []

for filter in range(numFilters):

    adjListFilters.append([])

    excludes = []

    for i in range(numCubes):
        excludes.append(0)
        adjListFilters[filter].append([])
        # for j in range(len(arrCube[i][filter])):
        # isValidZeros = not np.any(arrCube[i][filter])
            # if (not isValidZeros):
            #     break

        isValidZeros = zeroFilterFunction(arrCube[i][filter], percentThreshold)
        if (isValidZeros):
            zeroFilters += 1

    for cube1 in range(numCubes - 1):
        
        if (excludes[cube1] == 0):

            for cube2 in range(cube1 + 1, numCubes):

                if (excludes[cube2] == 0):
                    percentFilter = checkFilters(arrCube[cube1][filter], arrCube[cube2][filter])
                    allZeros1 = zeroFilterFunction(arrCube[cube1][filter], percentThreshold)
                    allZeros2 = zeroFilterFunction(arrCube[cube2][filter], percentThreshold)
                    if ((percentFilter >= percentThreshold) and (not allZeros1 and not allZeros2)):
                        if (excludes[cube1] == 0):
                            adjListFilters[filter][cube1].append(cube2)
                        else:
                            adjListFilters[filter][cube1].append(cube2)
                        excludes[cube1] = 1
                        excludes[cube2] = 1

excludes = []
adjListCubes = []
numMatches = 0
zeroCubes = 0

for i in range(numCubes):
    excludes.append(0)
    adjListCubes.append([])
    # for j in range(len(arrCube[i])):
    # isValidZeros = not np.any(arrCube[i])
        # if (not isValidZeros):
        #     break
    isValidZeros = zeroCubeFunction(arrCube[i], percentThreshold)
    if (isValidZeros):
        zeroCubes += 1

for cube1 in range(numCubes - 1):
    if (excludes[cube1] == 0):
        for cube2 in range(cube1 + 1, numCubes):
            if (excludes[cube2] == 0):
                percentCube = checkCubes(arrCube[cube1], arrCube[cube2])
                allZeros1 = zeroCubeFunction(arrCube[cube1], percentThreshold)
                allZeros2 = zeroCubeFunction(arrCube[cube2], percentThreshold)
                if ((percentCube >= percentThreshold) and (not allZeros1 and not allZeros2)):
                    if (excludes[cube1] == 0):
                        adjListCubes[cube1].append(cube2)
                    else:
                        adjListCubes[cube1].append(cube2)
                    excludes[cube1] = 1
                    excludes[cube2] = 1


finalNumFilters = 0
finalNumCubes = 0

for x in range(len(adjListFilters)):
    for y in range(len(adjListFilters[x])):
        finalNumFilters += len(adjListFilters[x][y])

for x in range(len(adjListCubes)):
    finalNumCubes += len(adjListCubes[x])

if (type == "tensor"):

    file = open(str(percentThreshold) + "% match.csv", 'a')
    writer = csv.writer(file)

    f = open('filtersandcubes.txt', 'a')

    shape = openingNP.shape

    row = ([shape, finalNumFilters, zeroFilters, finalNumCubes, zeroCubes])

    writer.writerow(row)

    f.write('\n')

    f.write(str(adjListFilters))
    f.write("\nComputations Saved for Filters Iterations: " + str(finalNumFilters))
    f.write("\nNumber of Zero Filters: " + str(zeroFilters))

    f.write('\n')

    f.write(str(adjListCubes))
    f.write("\nComputations Saved for Filters Cubes: " + str(finalNumCubes))
    f.write("\nNumber of Zero Cubes: " + str(zeroCubes))

    f.write('\n')

    file.close()
    f.close()

else:
    print(adjListFilters)
    print(adjListCubes)

    print (finalNumFilters, zeroFilters, finalNumCubes, zeroCubes)