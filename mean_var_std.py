import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(list).reshape(3, 3)
        mean_r = np.mean(matrix, axis=0)
        mean_c = np.mean(matrix, axis=1)
        mean_f = np.mean(matrix)
        var_r = np.var(matrix, axis=0)
        var_c = np.var(matrix, axis=1)
        var_f = np.var(matrix)
        std_r = np.std(matrix, axis=0)
        std_c = np.std(matrix, axis=1)
        std_f = np.std(matrix)
        max_r = np.max(matrix, axis=0)
        max_c = np.max(matrix, axis=1)
        max_f = np.max(matrix)
        min_r = np.min(matrix, axis=0)
        min_c = np.min(matrix, axis=1)
        min_f = np.min(matrix)
        sum_r = np.sum(matrix, axis=0)
        sum_c = np.sum(matrix, axis=1)
        sum_f = np.sum(matrix)
        calculations = {
            'mean': [mean_r.astype(float).tolist(), mean_c.astype(float).tolist(), float(mean_f)],
            'variance': [var_r.astype(float).tolist(), var_c.astype(float).tolist(), float(var_f)],
            'standard deviation': [std_r.astype(float).tolist(), std_c.astype(float).tolist(), float(std_f)],
            'max': [max_r.astype(float).tolist(), max_c.astype(float).tolist(), float(max_f)],
            'min': [min_r.astype(float).tolist(), min_c.astype(float).tolist(), float(min_f)],
            'sum': [sum_r.astype(float).tolist(), sum_c.astype(float).tolist(), float(sum_f)],
        }
    return calculations


print(calculate([9, 1, 5, 3, 3, 3, 2, 9, 0]))
