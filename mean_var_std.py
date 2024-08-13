import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    list_of_no = np.array(list).reshape(3, 3)
    
    calculations = {
        'mean': [list(np.mean(list_of_no, axis=0)), list(np.mean(list_of_no, axis=1)), np.mean(list_of_no).tolist()],
        'variance': [list(np.var(list_of_no, axis=0)), list(np.var(list_of_no, axis=1)), np.var(list_of_no).tolist()],
        'standard deviation': [list(np.std(list_of_no, axis=0)), list(np.std(list_of_no, axis=1)), np.std(list_of_no).tolist()],
        'max': [list(np.max(list_of_no, axis=0)), list(np.max(list_of_no, axis=1)), np.max(list_of_no).tolist()],
        'min': [list(np.min(list_of_no, axis=0)), list(np.min(list_of_no, axis=1)), np.min(list_of_no).tolist()],
        'sum': [list(np.sum(list_of_no, axis=0)), list(np.sum(list_of_no, axis=1)), np.sum(list_of_no).tolist()]
    }
    return calculations