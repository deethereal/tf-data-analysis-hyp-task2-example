import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 264956206  # Ваш chat ID, не меняйте название переменной
alpha = 0.02


def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    p_val = anderson_ksamp([x, y])[2]
    return p_val < alpha
