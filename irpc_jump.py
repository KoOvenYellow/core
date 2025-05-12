# irpc_jump.py
import math
from irpc_evaluator import evaluate_irpc

def irpc_vector(text):
    """
    文から IRPC ベクトル [I, R, P, C] を取得。
    """
    scores = evaluate_irpc(text)
    print(f"\nIRPC scores for: {text}")
    for k, v in scores.items():
        print(f"{k}: {v}")
    return [scores["Intent"], scores["Rhetoric"], scores["Predictability"], scores["Clarity"]]

def irpc_jump_probability(w1, w2, sigma=2.0):
    """
    2つの文に対する IRPC ベクトル間の距離に基づき、ジャンプ確率を計算。
    """
    v1 = irpc_vector(w1)
    v2 = irpc_vector(w2)
    if v1 is None or v2 is None:
        return 0.0
    min_len = min(len(v1), len(v2))
    v1 = v1[:min_len]
    v2 = v2[:min_len]
    squared_diff = sum((a - b) ** 2 for a, b in zip(v1, v2))
    return math.exp(-squared_diff / (sigma ** 2))
