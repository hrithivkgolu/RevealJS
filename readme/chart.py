import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------
# Data Generation
# ------------------------------

np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# Generate realistic response times (in minutes)
data = {
    "Channel": np.repeat(channels, 300),
    "ResponseTime": np.concatenate([
        np.random.normal(loc=120, scale=25, size=300),   # Email
        np.random.normal(loc=10, scale=4, size=300),     # Chat
        np.random.normal(loc=40, scale=12, size=300),    # Phone
        np.random.normal(loc=90, scale=20, size=300),    # Social Media
    ])
}

df = pd.DataFrame(data)

# ------------------------------
# Styling
# ------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 512x512 output at dpi=64

# ------------------------------
# Violinplot
# ------------------------------

sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="coolwarm",
    linewidth=1.2
)

plt.title("Customer Support Response Time Distribution by Channel", fontsize=18)
plt.xlabel("Support Channel")
plt.ylabel("Response Time (minutes)")

# ------------------------------
# Export
# ------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()