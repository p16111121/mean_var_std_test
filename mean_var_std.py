import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3, 3)

    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # 列均值
            matrix.mean(axis=1).tolist(),  # 行均值
            matrix.mean().tolist()         # 展平均值
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # 列方差
            matrix.var(axis=1).tolist(),   # 行方差
            matrix.var().tolist()          # 展平方差
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # 列標準差
            matrix.std(axis=1).tolist(),   # 行標準差
            matrix.std().tolist()          # 展平方標準差
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # 列最大值
            matrix.max(axis=1).tolist(),   # 行最大值
            matrix.max().tolist()          # 展平最大值
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # 列最小值
            matrix.min(axis=1).tolist(),   # 行最小值
            matrix.min().tolist()          # 展平最小值
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # 列總和
            matrix.sum(axis=1).tolist(),   # 行總和
            matrix.sum().tolist()          # 展平總和
        ]
    }

    return calculations