# irpc_evaluator.py

from openai import OpenAI
from dotenv import load_dotenv
import os
import re

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def evaluate_irpc(text):
    """
    Evaluate a sentence on four IRPC axes: Intent, Rhetoric, Predictability, Clarity.
    Returns a dictionary of scores (1–5).
    """
    prompt = f"""
You are a syntax evaluator. Evaluate the following sentence based on these 4 criteria, and return a score from 1 to 5 for each:

1. Intent
2. Rhetoric
3. Predictability
4. Clarity

Sentence: {text}

Format:
Intent: score
Rhetoric: score
Predictability: score
Clarity: score

Please respond strictly in English, using only the format specified
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content
    scores = {}
    labels = ["Intent", "Rhetoric", "Predictability", "Clarity"]
    for label in labels:
        match = re.search(f"{label}\\s*:\\s*(\\d)", content, re.IGNORECASE)
        if match:
            scores[label] = int(match.group(1))
    return scores

if __name__ == "__main__":
    test_sentence = "This service is a revolutionary solution that can transform your life from the ground up."
    result = evaluate_irpc(test_sentence)
    for k, v in result.items():
        print(f"{k}: {v}")
