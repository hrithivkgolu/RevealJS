"""
Generate a static HTML with an embedded PNG of the department-distribution
chart and print the Marketing department frequency count.

Email for verification: 24f2000717@ds.study.iitm.ac.in
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO, BytesIO
import base64

# Sample dataset (small example provided in the workspace)
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

# Load into DataFrame
df = pd.read_csv(StringIO(data))

# Calculate frequency count for Marketing department and print
marketing_count = df[df['department'] == 'Marketing'].shape[0]
print(f"Frequency count of Marketing department: {marketing_count}")

# Create histogram/countplot
plt.figure(figsize=(8,6))
sns.countplot(data=df, x='department', palette='viridis')
plt.title('Distribution of Employees Across Departments')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to PNG in memory
buf = BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
plt.close()
buf.seek(0)
img_b64 = base64.b64encode(buf.read()).decode('utf-8')

# Prepare HTML with embedded image and code block
code_snippet = '''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# (Data snippet omitted for brevity)'''

html_contents = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Department Distribution Visualization</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 24px; }}
        pre {{ background:#1e1e1e; color:#d4d4d4; padding:16px; border-radius:8px; overflow-x:auto; }}
        img {{ max-width:100%; height:auto; }}
    </style>
</head>
<body>
    <h2>Department Distribution Chart</h2>
    <div>
        <img src="data:image/png;base64,{img_b64}" alt="Department distribution histogram" />
    </div>
    <hr>
    <h3>Email for verification</h3>
    <p>24f2000717@ds.study.iitm.ac.in</p>
    <hr>
    <h3>Python Code Used (excerpt)</h3>
    <pre><code>{code_snippet}</code></pre>
</body>
</html>"""

# Write to the file named exactly as required by the validator
html_file = "department_distribution.html"
with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_contents)

print(f"HTML file '{html_file}' generated with embedded PNG image.")
