---
marp: true
theme: custom
paginate: true
title: Q4 2025 Earnings — Apex Financial Group
description: Q4 2025 Earnings (Marp)
author: Technical Consultant
---

<!-- Global footer (will show on every slide) -->
<!-- footer: 24f2000717@ds.study.iitm.ac.in -->

<!--
Custom theme CSS for Marp (this defines colors, footer and page-number style)
-->
<style>
/* --- Color variables --- */
:root{
  --bg-dark: #0f1620;
  --accent: #00d4aa;
  --muted: #6c7a89;
  --card: #ffffff;
}

/* --- Base slide styling --- */
section {
  font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
  color: #1b2730;
  background-color: #ffffff;
  padding: 48px;
}

/* --- Title / hero slide --- */
section.hero {
  background-color: var(--bg-dark);
  color: #fff;
}
section.hero h1 {
  font-size: 48px;
  margin-bottom: 6px;
}
section.hero h3 { color: rgba(255,255,255,0.85); font-weight: 500; }

/* --- Email styling used in slides and footer --- */
.email {
  color: var(--accent);
  font-weight: 700;
}

/* --- Small muted text --- */
.small-muted { color: var(--muted); font-size: 0.85em; }

/* --- Footer styles: override default paginate placement for clarity --- */
.marpify-footer {
  position: absolute;
  bottom: 12px;
  right: 18px;
  font-size: 0.85em;
  color: rgba(27,39,48,0.6);
}

/* --- Page numbers (paginate: true provides the number; style it) --- */
.marpify-footer .marp-pagination {
  color: rgba(27,39,48,0.6);
  font-weight: 500;
}

/* --- Card-like list style for visual slides --- */
.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(250,250,250,0.98));
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 8px 24px rgba(16,24,40,0.08);
}

/* --- Code block tweaks --- */
pre code {
  font-size: 0.9em;
  line-height: 1.45;
}

/* --- Math tweaks (KaTeX/Math rendering) --- */
.katex {
  font-size: 1.05em;
}
</style>

<!--
NOTE:
- The `footer:` directive above places the email on every slide (Marp will show it in the slide foot area).
- `paginate: true` shows page numbers. Styling above adjusts their appearance.
-->

# Q4 2025 Earnings Report  
### Apex Financial Group  
<span class="small-muted">Presented by Technical Consultant</span>

**Email:** <span class="email">24f2000717@ds.study.iitm.ac.in</span>  
**Date:** 28 February 2026

---

## Contact

If you have questions, please email:  
**<span class="email">24f2000717@ds.study.iitm.ac.in</span>**

---

<!-- slide with background image -->
<!--
backgroundImage: url('https://images.unsplash.com/photo-1542224566-0df5653b4d6f?q=80&w=1400&auto=format&fit=crop')
backgroundSize: cover
backgroundOpacity: 0.25
class: hero
-->

# Market Snapshot  
> Q4 visual context

This slide uses a full-bleed background image set through Marp slide-level directives.

---

## Financial Highlights — Q4 2025

<div class="card">

- **Net Income:** $2.87B (+28% YoY)  
- **EPS:** $4.62 (beat estimates by $0.31)  
- **Revenue:** $18.4B (+19% YoY)  
- **ROE:** 21.4%  
- **AUM:** $1.42T

</div>

> _"Strongest quarter in our 47-year history" — CEO_

---

## Key Growth Drivers

- Wealth Management: **+34% revenue**  
- Institutional Trading: **+27%**  
- Digital Assets division: **Launched**  
- Cost-to-income ratio: **54% (improved)**

---

## DuPont ROE (mathematical form)

DuPont decomposition shows drivers of ROE:

$$
\text{ROE} \;=\; \frac{\text{Net Income}}{\text{Revenue}} \times \frac{\text{Revenue}}{\text{Assets}} \times \frac{\text{Assets}}{\text{Equity}}
$$

- Increase in the first term (net margin) and leverage (Assets/Equity) explains ROE improvement.

---

## Algorithmic / Quant Math Example

Consider a divide-and-conquer quant routine (complexity analysis):

Recurrence:
$$
T(n) = 2\,T\left(\frac{n}{2}\right) + \Theta(n)
$$

By the Master Theorem:
$$
T(n) = \Theta(n\log n)
$$

Example: Sharpe computation (annualized):
```python
import numpy as np
returns = np.array([0.12, 0.08, 0.15, -0.03, 0.22, 0.18])
sharpe = (returns.mean() - 0.042) / returns.std() * np.sqrt(12)
print(f"Sharpe Ratio: {sharpe:.2f}")
