---
marp: true
theme: custom
math: true
paginate: true
title: MyProduct — Quick Reference
description: Example Marp deck with custom theme, background, math, and email
style: |
  /* Simple custom Marp theme */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
  section { font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; padding: 40px; }
  h1 { font-weight:700; letter-spacing: .02em; }
  .email { position: absolute; right: 1rem; bottom: 1rem; opacity: 0.9; font-size: 0.85rem; color: #2b7a78 }
  .lead { color: #213547; }
  .card { background: rgba(255,255,255,0.96); border-radius: 10px; padding: 18px; }
  .math { font-size: 1.05rem; }
---

<!-- Title slide -->
# MyProduct — Quick Reference

*Small, maintainable product documentation in Marp Markdown*

<div class="email">24f2000717@ds.study.iitm.ac.in</div>

---

<!-- Slide with local background image (relative path) -->
<!--
<!-- Slide with friendly 'welcome' background image (public Unsplash URL) -->
<!--
backgroundImage: url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1600&q=80')
backgroundSize: cover
backgroundOpacity: 0.65
class: lead
-->

# Visual: Product Hero

- This slide shows a full-bleed background image referenced relative to the Markdown file.
- Keep the image inside `markdownppt/` so the deck remains self-contained in the repo.

<div class="email">24f2000717@ds.study.iitm.ac.in</div>

---

## Why Markdown + Marp?

- Human-editable, reviewable in Git
- Export to PDF/HTML with Marp CLI or VS Code extension
- Easily maintain theme and slide-level directives

---

## Algorithmic Complexity (Math)

Consider the recurrence used in divide-and-conquer algorithms:

$$T(n)=a\,T\left(\frac{n}{b}\right)+f(n)$$

Master theorem (for $f(n)=\Theta(n^c)$):

$$T(n)=\begin{cases}
\Theta(n^{\log_b a}) & \text{if } c < \log_b a\\
\Theta(n^{\log_b a}\log n) & \text{if } c = \log_b a\\
\Theta(f(n)) & \text{if } c > \log_b a
\end{cases}$$

Example: Merge sort $\Rightarrow T(n)=\Theta(n\log n)$.

---

## Quick Code Example

```python
# NPV demonstration
def npv(cashflows, r):
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))

print(npv([-100000,30000,40000,50000,45000], 0.08))
```

---

## Exporting

- Preview in VS Code with Marp extension
- Export to PDF: `marp --pdf markdownppt/new_ppt.md`
- Export to HTML: `marp --html markdownppt/new_ppt.md`

---

<footer>Maintainer: 24f2000717@ds.study.iitm.ac.in</footer>
