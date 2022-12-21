import numpy as np
import csv
import openingNP

input = openingNP.arrCube

file = open('filtersandcubes.csv', 'a')
writer = csv.writer(file)

f = open('filtersandcubes.txt', 'a')

# file.write("Location: 8\n")

"""
EXPECTED OUTPUTS FOR HARD CODED INPUT:
(see below)

C1 F1 & C2 F1 = NO MATCH
C1 F1 & C3 F1 = MATCH
C2 F1 & C3 F1 = NO MATCH

C1 F2 & C2 F2 = MATCH
C1 F2 & C3 F2 = MATCH
C2 F2 & C3 F2 = MATCH

"""

# input = [
#     [ # CUBE 1
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
#     [ # CUBE 2
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
#     [ # CUBE 5
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
#     [ # CUBE 7
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

cThreshold = 100

def checkFilters(arr1, arr2):

    isValid = True
    allZeros = True

    count = 0

    for row in range(numX):
        for col in range(numY):
            if (arr1[row][col] != arr2[row][col]):
                isValid = False
            else:
                count += 1
                if (arr1[row][col] != 0):
                    allZeros = False



    percentFilter = (100*count)/(numX * numY)


    return isValid, allZeros, percentFilter

def checkCubes(arr1, arr2):

    isValid = True
    allZeros = True

    count = 0
    
    for filter in range(numFilters):
        isValid, allZeros, percentFilter = checkFilters(arr1[filter], arr2[filter])
        count += percentFilter*(numX*numY)

        if (isValid == False):
            break
    
    percentCube = (100*count)/(numFilters*numX*numY)

    return isValid, allZeros, percentCube

zeroFilters = 0
cubeMatching = 0
isValidZeros = True

adjListFilters = []

for filter in range(numFilters):

    adjListFilters.append([])

    excludes = []

    for i in range(numCubes):
        excludes.append(0)
        adjListFilters[filter].append([])
        for j in range(len(input[i][filter])):
            isValidZeros = not np.any(input[i][filter][j])
            if (not isValidZeros):
                break
        if (isValidZeros):
            zeroFilters += 1

    for cube1 in range(numCubes - 1):
        
        if (excludes[cube1] == 0):

            isValidZeros = True

            for cube2 in range(cube1 + 1, numCubes):

                if (excludes[cube2] == 0):
                    isFilterEqual, allZeros, percentFilter = checkFilters(input[cube1][filter], input[cube2][filter])
                    if (isFilterEqual and (not allZeros)):
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
    for j in range(len(input[i])):
        isValidZeros = not np.any(input[i][j])
        if (not isValidZeros):
            break
    if (isValidZeros):
        zeroCubes += 1

for cube1 in range(numCubes - 1):
    if (excludes[cube1] == 0):
        for cube2 in range(cube1 + 1, numCubes):
            if (excludes[cube2] == 0):

                isCubeEqual, allZeros, percentCube = checkCubes(input[cube1], input[cube2])

                if (isCubeEqual and (not allZeros)):
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


row = ([finalNumFilters, zeroFilters, finalNumCubes, zeroCubes])

writer.writerow(row)

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