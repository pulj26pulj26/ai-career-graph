import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

os.makedirs("docs/assets", exist_ok=True)

edges = ["M1", "M2", "M4"]
pure_vector = [0.58, 0.57, 0.57]
hybrid = [0.49, 0.43, 0.42]

x = range(len(edges))
width = 0.35

fig, ax = plt.subplots(figsize=(7, 4.5))
bars1 = ax.bar([i - width/2 for i in x], pure_vector, width,
               label="Pure Vector", color="#9aa5b1")
bars2 = ax.bar([i + width/2 for i in x], hybrid, width,
               label="Hybrid (semantic 0.7 / keyword 0.3)", color="#2f6feb")

for bars in (bars1, bars2):
    for bar in bars:
        h = bar.get_height()
        ax.annotate(f"{h:.2f}", (bar.get_x() + bar.get_width()/2, h),
                    ha="center", va="bottom", fontsize=9)

ax.set_xticks(list(x))
ax.set_xticklabels(edges)
ax.set_ylabel("Retrieval score")
ax.set_title("Edge retrieval: Pure Vector vs Hybrid\nM1-M2 gap: 0.01 -> 0.06", fontsize=11)
ax.set_ylim(0, 0.75)
ax.legend(loc="upper right", fontsize=8)
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("docs/assets/retrieval-comparison.png", dpi=150)
print("saved docs/assets/retrieval-comparison.png")