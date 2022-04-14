import numpy as np

def calculate(list):
    if len(list) != 9:
      raise ValueError("List must contain nine numbers.")
    #Convert list to array and reshape into 3X3 matrix
    matrix_array = np.array(list).reshape((3,3))
    #Nested Dictionaries
    calculations = {
      "mean": [
        np.mean(matrix_array, axis=0).tolist(),
        np.mean(matrix_array, axis=1).tolist(),
        np.mean(matrix_array).tolist()
      ],

      "variance": [
        np.var(matrix_array, axis=0).tolist(),
        np.var(matrix_array, axis=1).tolist(),
        np.var(matrix_array).tolist()
      ],

      "standard deviation": [
        np.std(matrix_array, axis=0).tolist(),
        np.std(matrix_array, axis=1).tolist(),
        np.std(matrix_array).tolist()
      ],

      "max": [
        np.max(matrix_array, axis=0).tolist(),
        np.max(matrix_array, axis=1).tolist(),
        np.max(matrix_array).tolist()
      ],

      "min": [
        np.min(matrix_array, axis=0).tolist(),
        np.min(matrix_array, axis=1).tolist(),
        np.min(matrix_array).tolist()
      ],

      "sum": [
        np.sum(matrix_array, axis=0).tolist(),
        np.sum(matrix_array, axis=1).tolist(),
        np.sum(matrix_array).tolist()
      ]
    }
    return calculations