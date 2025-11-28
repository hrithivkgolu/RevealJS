# Email for verification: 24f2000717@ds.study.iitm.ac.in

import matplotlib.pyplot as plt

# Quarterly MRR growth data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [3.5, 8.32, 8.22, 13.45]

# Industry benchmark
industry_target = 15

# Calculate average
average_mrr = sum(mrr_growth)/len(mrr_growth)
print(f"Average MRR Growth: {average_mrr:.2f}")

# Visualization: MRR Growth vs Industry Target
plt.figure(figsize=(8,5))
plt.plot(quarters, mrr_growth, marker='o', label='Company MRR Growth', color='blue')
plt.axhline(y=industry_target, color='red', linestyle='--', label='Industry Target (15)')
plt.title('Quarterly MRR Growth - 2024')
plt.xlabel('Quarter')
plt.ylabel('MRR Growth (%)')
plt.ylim(0, max(industry_target, max(mrr_growth)) + 5)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("mrr_growth_trend.png")
plt.show()