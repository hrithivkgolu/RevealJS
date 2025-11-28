---
marp: true
title: Product Documentation Overview
paginate: true
footer: "Apex Software · Product Docs · Page ${{ page }} of ${{ pages }}"
theme: custom
---

<!--
Custom Marp theme (embedded)
-->

<style>
section {
  font-family: 'Inter', sans-serif;
}

h1, h2 {
  color: #00d4aa;
}

custom-theme {
  background-color: #0f1620;
  color: white;
}
</style>

<!-- Define the custom theme -->
<style>
:root {
  --color-background: #0f1620;
  --color-foreground: #ffffff;
  --color-accent: #00d4aa;
}

section.custom {
  background: var(--color-background);
  color: var(--color-foreground);
}

section.custom h1 {
  color: var(--color-accent);
}
</style>

---

# **Product Documentation Presentation**
## Apex Software

**Technical Writer**  
📧 Email: **24f2000717@ds.study.iitm.ac.in**

---

# **Introduction**
This presentation documents the technical and product-level functionality of our software platform.  
It is written in **Marp**, suitable for:

- Version control (GitHub / GitLab)
- Automatic PDF conversion
- CI documentation pipelines
- Developer-friendly collaboration

---

<!-- Background image slide -->
<!-- Replace URL with your own repo's asset path if needed -->
![bg](https://images.unsplash.com/photo-1535223289827-42f1e9919769)

# **System Architecture**
Our platform follows a modular microservice structure enabling:

- Scalable deployments  
- Independent versioning  
- High-resilience service boundaries  

---

# **Algorithmic Complexity**
We use efficient algorithms in our query engine.

### Example: Time Complexity  
The complexity of a balanced binary search tree operation:

\[
T(n)=O(\log n)
\]

The complexity of a naive search:

\[
T(n)=O(n)
\]

Mathematically, for input size \( n \):

\[
\text{Improvement Ratio} = \frac{O(n)}{O(\log n)} = \frac{n}{\log n}
\]

---

# **Custom Styling Example**

<style>
.custom-box {
  padding: 20px;
  border: 2px solid #00d4aa;
  border-radius: 12px;
  color: #00d4aa;
  font-size: 1.2em;
  background: rgba(0,212,170,0.1);
}
</style>

<div class="custom-box">
  This container is styled using custom CSS inside the Marp document.
</div>

---

# **Deployment Flow**
1. Write documentation in Markdown  
2. Commit to GitHub  
3. Use Marp CLI or GitHub Actions to generate:  
   - PDF  
   - PPTX  
   - HTML  
4. Publish to Docs Portal  

---

# **Thank You**
Questions?  
📧 **24f2000717@ds.study.iitm.ac.in**

---