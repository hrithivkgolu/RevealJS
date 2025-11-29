---
marp: true
theme: custom
paginate: true
footer: "Apex Software · Product Docs · Page ${{ page }} of ${{ pages }}"
title: Product Documentation Overview
description: "Technical documentation presentation for Apex Software"
---

<!-- class: custom -->

<!--
Embedded Custom Marp Theme
Use with: marp --theme custom.css <file>.md
-->

<style>
:root {
  --color-background: #0f1620;
  --color-foreground: #ffffff;
  --color-accent: #00d4aa;
  --color-accent-light: rgba(0, 212, 170, 0.1);
}

section {
  background: var(--color-background);
  color: var(--color-foreground);
  font-family: 'Inter', sans-serif;
}

h1, h2 {
  color: var(--color-accent);
}

/* Custom styled box */
.custom-box {
  padding: 20px;
  border: 2px solid var(--color-accent);
  border-radius: 12px;
  color: var(--color-accent);
  font-size: 1.2em;
  background: var(--color-accent-light);
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
![bg](https://images.unsplash.com/photo-1535223289827-42f1e9919769)

# **System Architecture**
Our platform follows a modular microservice structure enabling:

- Scalable deployments  
- Independent versioning  
- High-resilience service boundaries  

---

# **Algorithmic Complexity**
### Example: Time Complexity

\[
T(n)=O(\log n)
\]

Naive search:

\[
T(n)=O(n)
\]

Improvement ratio:

\[
\frac{n}{\log n}
\]

---

# **Custom Styling Example**

<div class="custom-box">
  This container is styled using custom CSS inside the Marp document.
</div>

---

# **Deployment Flow**
1. Write documentation in Markdown  
2. Commit to GitHub  
3. Generate PDF / PPTX / HTML via Marp CLI or GitHub Actions  
4. Publish to Docs Portal  

---

# **Thank You**
Questions?  
📧 **24f2000717@ds.study.iitm.ac.in**

