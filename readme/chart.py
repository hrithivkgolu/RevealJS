import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Synthetic business data generation ---
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]
data = {
    "channel": np.repeat(channels, 250),
    "response_time": np.concatenate([
        np.random.normal(6, 2, 250),   # Email (slow)
        np.random.normal(2, 0.7, 250), # Chat (fast)
        np.random.normal(4, 1.2, 250), # Phone
        np.random.normal(8, 3, 250),   # Social Media (slowest)
    ])
}

df = pd.DataFrame(data)

# --- Professional Seaborn styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Create EXACT 512x512 PNG ---
fig = plt.figure(figsize=(512/100, 512/100), dpi=100)

sns.violinplot(
    data=df,
    x="channel",
    y="response_time",
    palette="Set2",
    cut=0
)

plt.title("Response Time Distribution by Support Channel")
plt.xlabel("Support Channel")
plt.ylabel("Response Time (hours)")

# Remove extra padding to preserve exact size
plt.tight_layout(pad=0)

# Save EXACT 512x512
plt.savefig("chart.png", dpi=100)
plt.close()