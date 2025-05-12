# jump.py
import numpy as np
from .syntax import syntax_vector  # ファイル名に応じて変更してね

def jump_probability(w1: str, w2: str, sigma: float = 1.0) -> float:
    """
    Calculate the probability of a syntax jump from sentence w1 to w2
    using the formula:
    
    P(W1 -> W2) = exp( - ||C(W1) - C(W2)||^2 / sigma^2 )
    
    where C(W) is the syntax vector of sentence W.
    """
    v1 = syntax_vector(w1)
    v2 = syntax_vector(w2)
    
    # 距離の調整（次元数の違いを考慮）
    min_len = min(len(v1), len(v2))
    v1 = v1[:min_len]
    v2 = v2[:min_len]
    
    distance_squared = np.sum((v1 - v2)**2)
    prob = np.exp(-distance_squared / (sigma**2))
    return float(prob)
