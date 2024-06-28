import numpy as np
import random
def gauss_elimination(matA, matb):

    # Converting into the numpy vectors
    A = np.array(matA, dtype='float64')
    B = np.array(matb, dtype='float64')

    sizeA = np.size(A, 1)
    # Combining the two matrix to form Augmented matrix
    AB = np.concatenate((A, B), 1)
    n = np.size(AB, 0)
    m = np.size(AB, 1)
    x = np.zeros(n)
    arbitrary_value = random.random()

    # Elimination Step:

    for i in range(0, sizeA - 1):
        AB[i + 1] = AB[i + 1] - (AB[i + 1, 0] / AB[0, 0]) * AB[0]

    for j in range(sizeA - 1):
        for k in range(0, j):
            AB[j + 1] = AB[j + 1] - (AB[j + 1, k + 1] / AB[j, k + 1]) * AB[j]


    # Back Substitution method

    for i in range(n - 1, -1, -1):
        if AB[i, i] != 0:
            x[i] = (AB[i, n] - np.dot(AB[i, i + 1:m - 1], x[i + 1:n])) / AB[i, i]
        else:
            x[i] = arbitrary_value
            print("This is the case of Infinitely many solution")

    print(f"The solution to the given system of linear equation is: {x}")

