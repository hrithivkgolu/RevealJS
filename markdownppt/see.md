<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quarterly Earnings — Interactive Reveal.js Presentation</title>

  <!-- Reveal.js core styles -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
  <!-- Theme (you can swap with black, white, league, solarized) -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/solarized.css" id="theme">

  <!-- Highlight.js for code highlighting (used by Reveal's highlight plugin) -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">

  <style>
    /* Small custom styling */
    .footer-email {
      position: absolute;
      right: 20px;
      bottom: 10px;
      font-size: 0.9rem;
      opacity: 0.85;
    }
    .logo-title {
      font-weight: 700;
      letter-spacing: 0.02em;
    }
    /* Make fragments animate slightly smoother */
    .fragment {
      transition: opacity 300ms ease, transform 300ms ease;
    }
  </style>
</head>
<body>

  <div class="reveal">
    <div class="slides">

      <!-- Title slide -->
      <section>
        <h1 class="logo-title">Quarterly Earnings — Q3</h1>
        <h3>Financial Institution — Stakeholder Presentation</h3>
        <p>Prepared by: Technical Consulting</p>
        <p class="footer-email">Contact: 24f2000717@ds.study.iitm.ac.in</p>
        <aside class="notes">
          Introduce the team, set expectations for the 20-minute walkthrough. Mention that detailed model outputs are available after the live session.
        </aside>
      </section>

      <!-- Background image slide -->
      <section data-background-image="sample-bg.jpg" data-background-size="cover" data-background-opacity="0.35">
        <h2 style="background: rgba(0,0,0,0.4); padding: 10px; border-radius: 8px; color: white;">Market Snapshot — Background Image Demo</h2>
        <p class="fragment" style="color: white; text-shadow: 0 0 5px black;">This slide includes a full background image.</p>
        <aside class="notes">
          Demonstrate that Reveal.js can use background images per slide using data-background-image attributes.
        </aside>
      </section>

      <!-- Markdown slide (demonstrates data in markdown) -->
      <section data-markdown>
        <script type="text/template">

# Executive Highlights (Markdown)

- **Revenue (QoQ):** +6.2%  
- **Net Interest Margin:** 2.85%  
- **Cost-to-Income Ratio:** 48%  

> This slide was authored in **Markdown** — demonstrates flexible content editing for stakeholders.

1. Action Item: Approve incremental budget for digital initiatives.
2. Action Item: Review risk-weighted asset assumptions.

        </script>
        <aside class="notes">
          Use this slide to demonstrate how content can be edited quickly by non-developers using plain Markdown.
        </aside>
      </section>

      <!-- Flow/Animated fragments slide -->
      <section>
        <h2>Customer Conversion Funnel (Animated)</h2>
        <ul>
          <li class="fragment">Awareness — 120,000</li>
          <li class="fragment">Interest — 45,200</li>
          <li class="fragment">Consideration — 18,900</li>
          <li class="fragment">Application — 6,300</li>
          <li class="fragment">Purchase / Onboarded — 2,850</li>
        </ul>
        <aside class="notes">
          Progress through each fragment to reveal funnel counts. Emphasize drop-off points and conversion opportunities.
        </aside>
      </section>

      <!-- Code sample slide with syntax highlighting -->
      <section>
        <h2>Sample: NPV Calculation (Python)</h2>
        <pre><code data-trim class="language-python">def npv(cashflows, discount_rate):
    """Compute net present value for a stream of cashflows.

    cashflows: list of numbers (CF0, CF1, CF2, ...)
    discount_rate: decimal (eg. 0.05 for 5%)
    """
    return sum(cf / ((1 + discount_rate) ** n) for n, cf in enumerate(cashflows))

# Example
cashflows = [-100000, 30000, 40000, 50000, 45000]
print("NPV:", npv(cashflows, 0.08))
</code></pre>
        <aside class="notes">
          Walk through how NPV is coded and which assumptions (discount rate, horizon) drive sensitivity.
        </aside>
      </section>

      <!-- Mathematical equations slide -->
      <section>
        <h2>Key Financial Formulas</h2>
        <p>
          Present Value of a future cashflow:
        </p>
        <p>
          $$PV = \frac{CF}{(1 + r)^n}$$
        </p>
        <p class="fragment">
          Net Present Value of a stream: 
        </p>
        <p class="fragment">
          $$NPV = \sum_{t=0}^{T} \frac{CF_t}{(1 + r)^t}$$
        </p>
        <aside class="notes">
          Explain the interpretation of discount rate r and horizon T. Tie to enterprise WACC and scenario analysis.
        </aside>
      </section>

      <!-- Slide showing JavaScript snippet and fragment animation -->
      <section>
        <h2>Realtime KPI Widget (JS)</h2>
        <pre><code data-trim class="language-js">// Fetch KPI from internal API and update the dashboard
async function fetchKPI() {
  const resp = await fetch('/api/v1/kpi');
  const data = await resp.json();
  document.getElementById('kpi-value').textContent = data.kpi;
}

setInterval(fetchKPI, 30_000); // refresh every 30s
</code></pre>

        <p id="kpi-value" class="fragment">(Live KPI will appear here during demo)</p>
        <aside class="notes">
          This slide demonstrates embedding code samples and describing how the live dashboard updates work. Clarify security and API throttling concerns.
        </aside>
      </section>

      <!-- Closing slide -->
      <section>
        <h2>Questions & Next Steps</h2>
        <ol>
          <li class="fragment">Approve Q4 budget reallocations</li>
          <li class="fragment">Run stress test with alternative macro scenarios</li>
          <li class="fragment">Schedule deep-dive with risk team</li>
        </ol>
        <p class="footer-email">Contact: 24f2000717@ds.study.iitm.ac.in</p>
        <aside class="notes">
          End with clear asks and an invitation for follow-up sessions. Provide stakeholders with the deck and the raw data repository link.
        </aside>
      </section>

    </div>
  </div>

  <!-- Reveal core JS -->
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.min.js"></script>
  <!-- Plugins -->
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/markdown/markdown.esm.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/highlight.esm.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/notes/notes.esm.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/math/math.esm.js"></script>

  <!-- MathJax for rendering LaTeX (used by the math plugin) -->
  <script>
    window.MathJax = {
      tex: { inlineMath: [['$','$'], ['\\(','\\)']] },
      svg: { fontCache: 'global' }
    };
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js" integrity="" crossorigin="anonymous"></script>

  <script>
    // Initialize Reveal with plugins
    Reveal.initialize({
      hash: true,
      slideNumber: true,
      plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealMath ],
      // Configure math plugin to use MathJax 3
      math: {
        mathjax: 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js'
      }
    });
  </script>
</body>
</html>
