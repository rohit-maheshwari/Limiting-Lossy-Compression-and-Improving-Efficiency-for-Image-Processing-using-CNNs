import numpy as np

# data = np.random.normal(0, 1, 100)
# np.save('tensor.npy', data)

type = input("Would you like to use test or tensor?\n")
percentThreshold = int(input("Enter the percent threshold: "))

if (type == "tensor"):
    tensorNum = input("Enter tensor number: ")
    arrCube = np.load("tensor" + str(tensorNum) + ".npy")

    shape = arrCube.shape

    arrCube = np.rollaxis(arrCube, 3, 1)

    print(arrCube)

    print(arrCube.shape)

    arrCube = arrCube.tolist()
    # print(arrCube)
else:

    # arrCube = [
    #     [
    #         [
    #             [1,1,0],[0,0,0],[0,0,0]
    #         ]
    #     ],
    #     [
    #         [
    #             [1,1,0],[0,0,0],[0,0,0]
    #         ]
    #     ]
    # ]

    arrCube = [
        [ # CUBE 0
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ], 
        [ # CUBE 1
            [
                [
                    11,
                    12,
                    13
                ],
                [
                    14,
                    15,
                    16
                ],
                [
                    17,
                    18,
                    19
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ],
        [ # CUBE 2
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ],
        [ # CUBE 3
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ],
        [ # CUBE 4
            [
                [
                    11,
                    12,
                    13
                ],
                [
                    14,
                    15,
                    16
                ],
                [
                    17,
                    18,
                    19
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ],
        [ # CUBE 5
            [
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ]
            ],
            [
                [
                    1,
                    2,
                    3
                ],
                [
                    4,
                    5,
                    6
                ],
                [
                    7,
                    8,
                    9
                ]
            ]
        ],
        [ # CUBE 6
            [
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ]
            ],
            [
                [
                    1,
                    2,
                    0
                ],
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ]
            ]
        ],
        [ # CUBE 7
            [
                [
                    1,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ]
            ],
            [
                [
                    0,
                    0,
                    2
                ],
                [
                    2,
                    2,
                    2
                ],
                [
                    2,
                    2,
                    2
                ]
            ]
        ],
        [ # CUBE 8
            [
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ],
                [
                    0,
                    0,
                    0
                ]
            ],
            [
                [
                    0,
                    0,
                    1
                ],
                [
                    1,
                    1,
                    1
                ],
                [
                    1,
                    1,
                    1
                ]
            ]
        ],
    ]