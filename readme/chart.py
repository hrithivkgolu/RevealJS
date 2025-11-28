import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

# -------------------------
# Synthetic data generation
# -------------------------
np.random.seed(42)

channels = ["Email", "Chat", "Phone", "Social Media"]

# realistic response times in minutes (skewed where appropriate)
n_per_channel = 350
data = {
    "Channel": np.repeat(channels, n_per_channel),
    "ResponseTime": np.concatenate([
        np.random.lognormal(mean=np.log(120), sigma=0.25, size=n_per_channel),  # Email (long tail, slower)
        np.random.normal(loc=8, scale=2.0, size=n_per_channel),                 # Chat (fast)
        np.random.lognormal(mean=np.log(40), sigma=0.3, size=n_per_channel),   # Phone (some tail)
        np.random.lognormal(mean=np.log(90), sigma=0.35, size=n_per_channel),  # Social Media
    ])
}
df = pd.DataFrame(data)

# keep values positive and reasonable
df["ResponseTime"] = df["ResponseTime"].clip(lower=0.5, upper=1440)

# -------------------------
# Styling & plot creation
# -------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # presentation-ready text sizes
palette = sns.color_palette("Set2")

# Render at high resolution first to avoid aliasing issues when downsampling
TARGET_PX = 512
LARGE_PX = 2048  # render larger then downsample (4x recommended)
dpi = 300
figsize = (LARGE_PX / dpi, LARGE_PX / dpi)

fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

# Fill the axes nicely but leave a bit of room for labels/title
sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette=palette,
    cut=0,
    inner="quartile",
    linewidth=1.0,
    ax=ax
)

ax.set_title("Response Time Distribution by Support Channel", fontsize=22, pad=12)
ax.set_xlabel("Support Channel", fontsize=16)
ax.set_ylabel("Response Time (minutes)", fontsize=16)

# Tweak tick params for readability
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Optionally log-scale y-axis if distributions are highly skewed.
# Uncomment the next line if you prefer log scale:
# ax.set_yscale('log')

# Make sure plot uses the full canvas but keep labels visible
plt.tight_layout()

# Save to an in-memory buffer at high resolution
buf = io.BytesIO()
fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight', pad_inches=0.02)
plt.close(fig)
buf.seek(0)

# -------------------------
# Post-process: crop & resize to EXACT 512x512
# -------------------------
img = Image.open(buf).convert("RGBA")

# center-crop to square based on the smaller dimension (handles any extra padding)
w, h = img.size
min_side = min(w, h)
left = (w - min_side) // 2
top = (h - min_side) // 2
right = left + min_side
bottom = top + min_side
img_cropped = img.crop((left, top, right, bottom))

# Resize with high-quality resampling
img_resized = img_cropped.resize((TARGET_PX, TARGET_PX), resample=Image.LANCZOS)

# Convert to RGB and save final PNG
img_final = img_resized.convert("RGB")
img_final.save("chart.png", format="PNG")

print("chart.png generated — exact size:", img_final.size)