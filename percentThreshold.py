import numpy as np
import csv
import openingNP

input = openingNP.arrCube
shape = openingNP.shape

file = open('66% match.csv', 'a')
writer = csv.writer(file)

f = open('filtersandcubes.txt', 'a')


# input = [
#     [ # CUBE 0
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ], 
#     [ # CUBE 1
#         [
#             [
#                 11,
#                 12,
#                 13
#             ],
#             [
#                 14,
#                 15,
#                 16
#             ],
#             [
#                 17,
#                 18,
#                 19
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ],
#     [ # CUBE 2
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ],
#     [ # CUBE 3
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ],
#     [ # CUBE 4
#         [
#             [
#                 11,
#                 12,
#                 13
#             ],
#             [
#                 14,
#                 15,
#                 16
#             ],
#             [
#                 17,
#                 18,
#                 19
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ],
#     [ # CUBE 5
#         [
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 3
#             ],
#             [
#                 4,
#                 5,
#                 6
#             ],
#             [
#                 7,
#                 8,
#                 9
#             ]
#         ]
#     ],
#     [ # CUBE 6
#         [
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ],
#         [
#             [
#                 1,
#                 2,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ]
#     ],
#     [ # CUBE 7
#         [
#             [
#                 1,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ],
#         [
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ]
#     ],
#     [ # CUBE 8
#         [
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ],
#         [
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ],
#             [
#                 0,
#                 0,
#                 0
#             ]
#         ]
#     ],
# ]


numCubes = len(input) # 16
numFilters = len(input[0]) # 16
numX = len(input[0][0]) # 3
numY = len(input[0][0][0]) # 3

percentThreshold = 66

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

def zeroFilterFunction(arr):

    allZeros = True

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] != 0):
                allZeros = False
                return allZeros
    
    return allZeros


def zeroCubeFunction(arr):

    allZeros = True

    for x in range(len(arr)):
        for i in range(len(arr[x])):
            for j in range(len(arr[x][i])):
                if (arr[x][i][j] != 0):
                    allZeros = False
                    return allZeros

    return allZeros

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
        # for j in range(len(input[i][filter])):
        isValidZeros = not np.any(input[i][filter])
            # if (not isValidZeros):
            #     break
        if (isValidZeros):
            zeroFilters += 1

    for cube1 in range(numCubes - 1):
        
        if (excludes[cube1] == 0):

            for cube2 in range(cube1 + 1, numCubes):

                if (excludes[cube2] == 0):
                    percentFilter = checkFilters(input[cube1][filter], input[cube2][filter])
                    allZeros1 = zeroFilterFunction(input[cube1][filter])
                    allZeros2 = zeroFilterFunction(input[cube2][filter])
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
    # for j in range(len(input[i])):
    isValidZeros = not np.any(input[i])
        # if (not isValidZeros):
        #     break
    if (isValidZeros):
        zeroCubes += 1

for cube1 in range(numCubes - 1):
    if (excludes[cube1] == 0):
        for cube2 in range(cube1 + 1, numCubes):
            if (excludes[cube2] == 0):
                percentCube = checkCubes(input[cube1], input[cube2])
                allZeros1 = zeroCubeFunction(input[cube1])
                allZeros2 = zeroCubeFunction(input[cube2])
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

# print(adjListFilters)
# print(adjListCubes)

# print (finalNumFilters, zeroFilters, finalNumCubes, zeroCubes)