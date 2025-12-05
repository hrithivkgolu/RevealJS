---
marp: true
theme: custom
paginate: true
title: Product Documentation — MyProduct
description: Maintainable product docs written in Marp Markdown
style: |
  /* Custom Marp theme styles */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
  section { font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; }
  h1.logo { letter-spacing: .02em; font-weight:700; }
  .email { position: absolute; right: 1rem; bottom: 1rem; opacity: 0.85; font-size: 0.9rem; }
  .lead { color: #213547; }
  .complexity { font-family: 'Courier New', monospace; background: rgba(33,53,71,0.04); padding: .35em .6em; border-radius: 6px; }
  section .bg-svg { position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1; }
  footer { font-size: 0.8rem; opacity: 0.8; }
---

<!-- Slide 1: Title -->
# MyProduct — Technical Documentation

*Maintainable source in Markdown — exportable with Marp tools*

---

<!-- Footer email shown on every slide via explicit block (keeps it in repo-friendly Markdown) -->
<div class="email">24f2000717@ds.study.iitm.ac.in</div>

---

<!-- Slide 2: Background image slide (SVG embedded inline in this file) -->
<!-- We embed an inline SVG so the image is kept in the same file and remains repo-friendly. -->
<svg class="bg-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0" stop-color="#5ee7df"/>
      <stop offset="1" stop-color="#b490ca"/>
    </linearGradient>
    <filter id="grain" x="-50%" y="-50%" width="200%" height="200%">
      <feTurbulence baseFrequency="0.8" numOctaves="2" stitchTiles="stitch" result="t"/>
      <feColorMatrix type="saturate" values="0"/>
      <feBlend in="SourceGraphic"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#g)"/>
  <g opacity="0.12">
    <text x="50%" y="52%" dominant-baseline="middle" text-anchor="middle" font-size="160" fill="#ffffff">MyProduct</text>
  </g>
</svg>

# Visual Overview — Background embedded in-file

- This slide demonstrates an inline SVG used as a background image, so the image is stored in the same Markdown file (no external asset required).

---

<!--
<!--
backgroundImage: url('45FA21E0-CE2C-42C4-8446-FB127D3B061D_1_105_c.jpeg')
backgroundSize: cover
backgroundOpacity: 0.95
-->

# Slide with explicit background image

- This slide uses a Marp slide directive (`backgroundImage`) with a data-URI SVG so the background is defined per-slide and kept in the same Markdown file.

---

<!-- Slide 3: Quick start / purpose -->
## Purpose

- **Audience:** Engineers, Product, and Technical Writers
- **Goal:** Keep product docs version-controlled and exportable to PDF or slides

---

<!-- Slide 4: Mathematical equations (algorithmic complexity) -->
## Algorithmic Complexity Examples

Consider a recurrence frequently seen in divide-and-conquer algorithms:

$$T(n) = a\\,T\\left(\\frac{n}{b}\\right) + f(n)$$

By the Master Theorem, when $f(n)=\\Theta(n^c)$:

$$T(n)=\\begin{cases}
\\Theta(n^{\\log_b a}) & \\text{if } c < \\log_b a\\\\
\\Theta(n^{\\log_b a}\\log n) & \\text{if } c = \\log_b a\\\\
\\Theta(f(n)) & \\text{if } c > \\log_b a
\\end{cases}$$

Example: Merge Sort has $a=2$, $b=2$, $f(n)=\\Theta(n)$ so $T(n)=\\Theta(n\\log n)$.

---

<!-- Slide 5: Complexity summary block -->
## Complexity Cheat Sheet

- Linear search: $\\;O(n)$
- Binary search: $\\;O(\\log n)$
- Merge sort: $\\;O(n\\log n)$
- Hash table (avg): $\\;O(1)$

```text
Space / time notes: balance readability vs. performance.
```

---

<!-- Slide 6: Code sample -->
## Example: NPV (Python)

```python
def npv(cashflows, r):
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cashflows))

print(npv([-100000,30000,40000,50000,45000], 0.08))
```

---

## Export & Conversion

- Use `marp --pdf file.md` to export to PDF
- Use `marp --html file.md` to export static HTML

---

## Contact & Maintainer

- Email: `24f2000717@ds.study.iitm.ac.in`
- Keep this file small and review SVG if you need a larger image asset separated.

---

<!-- End of slides -->

