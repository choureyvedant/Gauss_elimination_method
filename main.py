from Gauss_Elimination import gauss_elimination
import numpy as np

# Example
matA = np.array([[5, 2, 3],[4, 3, 2],[6, 2, 4]])
matb = np.array([[13.50],[12],[16]])
sol_equations = gauss_elimination(matA,matb)
