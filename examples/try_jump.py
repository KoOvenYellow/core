import sys
import os

# 現在のファイルの親ディレクトリをモジュールパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from syndo.jump import jump_probability

pairs = [
    ("I see fire", "I see light"),
    ("Syntax is action", "Bananas are blue"),
    ("Structure forms meaning", "Structure destroys meaning"),
    ("Hello world", "Goodbye sun"),
    ("This is a sentence", "This is another sentence"),
]

print("\n--- Syntax Jump Probabilities ---\n")

for w1, w2 in pairs:
    p = jump_probability(w1, w2, sigma=10.0)
    print(f"P({w1!r} → {w2!r}) = {p:.4f}")
