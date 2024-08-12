import numpy as np

def calculate(list):
    # 1. Check if the input list contains exactly 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Convert the list into a 3x3 Numpy array
    array = np.array(list).reshape(3, 3)

    # 3. Calculate the required statistics
    calculations = {
        'mean': [
            np.mean(array, axis=0).tolist(),
            np.mean(array, axis=1).tolist(),
            np.mean(array).tolist()
        ],
        'variance': [
            np.var(array, axis=0).tolist(),
            np.var(array, axis=1).tolist(),
            np.var(array).tolist()
        ],
        'standard deviation': [
            np.std(array, axis=0).tolist(),
            np.std(array, axis=1).tolist(),
            np.std(array).tolist()
        ],
        'max': [
            np.max(array, axis=0).tolist(),
            np.max(array, axis=1).tolist(),
            np.max(array).tolist()
        ],
        'min': [
            np.min(array, axis=0).tolist(),
            np.min(array, axis=1).tolist(),
            np.min(array).tolist()
        ],
        'sum': [
            np.sum(array, axis=0).tolist(),
            np.sum(array, axis=1).tolist(),
            np.sum(array).tolist()
        ]
    }
    return calculations
print(calculate([0,1,2,3,4,5,6,7,8]))
print(calculate([3, 5, 7, 9, 11, 13, 15, 17, 19]))
