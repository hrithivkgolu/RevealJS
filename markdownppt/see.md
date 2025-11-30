---
marp: true
title: Data Design by Dialogue
author: Anand S
theme: gaia
paginate: true
---

<style>
  blockquote {
    font-style: italic;
  }
  section {
    background-image: url('qr-code.png');
    background-repeat: no-repeat;
    background-position: top 20px right 20px;
    background-size: 80px auto;
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