import numpy as np

def calculate(list):
    if len(list) != 9:
         raise ValueError('List must contain nine numbers ')
    else:
        new_list = np.array(list)
        new_list = np.reshape(new_list,[3,3])

        calculations = {
        'mean' : [np.mean(new_list, axis=0).tolist(), np.mean(new_list, axis=1).tolist(), np.mean(list)],
        'variance' : [np.var(new_list, axis=0).tolist(), np.var(new_list, axis=1).tolist(), np.var(list)],
        'standard deviation' : [np.std(new_list, axis=0).tolist(), np.std(new_list, axis=1).tolist(), np.std(list)],
        'max' : [np.max(new_list, axis=0).tolist(), np.max(new_list, axis=1).tolist(), np.max(list)],
        'min' : [np.min(new_list, axis=0).tolist(), np.min(new_list, axis=1).tolist(), np.min(list)],
        'sum' : [np.sum(new_list, axis=0).tolist(), np.sum(new_list, axis=1).tolist(), np.sum(list)]
        }  
        return calculations
