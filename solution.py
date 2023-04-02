import pandas as pd
import numpy as np


chat_id = 291445198 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return np.mean(np.log(x - 667))
