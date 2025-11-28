# Email for verification: 24f2000717@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from io import StringIO

# Sample dataset
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,R&D,Middle East,75.23,2,4.7
EMP002,R&D,North America,82.72,1,4.8
EMP003,HR,Africa,75.47,7,4
EMP004,Finance,North America,71.42,7,4.9
EMP005,IT,North America,72.95,12,3.8
EMP006,Marketing,Europe,68.5,3,4.2
EMP007,Marketing,Asia,77.8,5,4.5
EMP008,IT,Africa,79.1,4,4.1
EMP009,Finance,Middle East,74.3,6,4.6
EMP010,HR,Europe,80.2,2,4.3"""

# Load data into a DataFrame
df = pd.read_csv(StringIO(data))

# Frequency count for Marketing department
marketing_count = df[df['department'] == 'Marketing'].shape[0]
print(f"Frequency count of Marketing department: {marketing_count}")

# Create a histogram of departments
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='department', palette='viridis')
plt.title('Distribution of Employees Across Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()

# Convert plot to HTML using mpld3
html_str = mpld3.fig_to_html(plt.gcf())

# Embed email for verification inside the HTML
email_html = "<p>Email for verification: 24f2000717@ds.study.iitm.ac.in</p>"
html_str_with_email = html_str.replace("</body>", email_html + "</body>")

# Save the HTML file
html_file = "department_distribution.html"
with open(html_file, "w") as f:
    f.write(html_str_with_email)

print(f"HTML file '{html_file}' generated successfully with email embedded!")
