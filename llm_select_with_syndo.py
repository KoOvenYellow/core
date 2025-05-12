# llm_select_with_syndo.py
from openai import OpenAI
from dotenv import load_dotenv
import os
from irpc_jump import irpc_jump_probability
from irpc_evaluator import evaluate_irpc

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_candidates(prompt, n=5):
    """
    GPTにn個の出力候補を生成させる。
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        n=n
    )
    return [choice.message.content for choice in response.choices]

def select_best_candidate(w1, candidates, sigma=2.0):
    """
    各候補に対するジャンプ確率を計算し、最も高いものを返す。
    """
    best_p = -1
    best_w2 = ""
    for w2 in candidates:
        p = irpc_jump_probability(w1, w2, sigma)
        print(f"→ {w2}\n   P = {p:.4f}\n")
        if p > best_p:
            best_p = p
            best_w2 = w2
    return best_w2, best_p

if __name__ == "__main__":
    w1 = "このサービスは、あなたの生活を根本から変える革新的なソリューションです。"
    instruction = "この文に続く適切な次の一文を提案してください。"

    print("=== IRPC scores for source sentence ===")
    w1_scores = evaluate_irpc(w1)
    for k, v in w1_scores.items():
        print(f"{k}: {v}")
    print("========================================\n")

    prompt = f"{w1}\n\n{instruction}"
    
    candidates = generate_candidates(prompt, n=5)
    best, score = select_best_candidate(w1, candidates)

    print("\n🔥 最もジャンプ確率の高い候補：")
    print(f"{best}\n(P = {score:.4f})")
