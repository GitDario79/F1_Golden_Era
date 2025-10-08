# F1 Golden Era – Quantifying “Action” in Formula 1

![tests](https://img.shields.io/github/actions/workflow/status/GitDario79/F1_Golden_Era/python.yml?label=tests)
![license](https://img.shields.io/badge/license-MIT-informational)
![python](https://img.shields.io/badge/python-3.11+-blue)

This project performs a data-driven analysis of historical Formula 1 data (1950–2021) to quantify how “action-packed” races and eras were.  
Instead of relying on subjective impressions, it compares **qualifying grid** vs **race results** and uses lap-level metrics to score unpredictability.

> _Optional preview image goes here once you add it:_  
> `![App preview](docs/summary.png)`

---

## Metrics

- **Position Volatility Index (PVI):** mean absolute lap-to-lap position change per driver, averaged across drivers within a race (then averaged across races in a season).  
- **Lead-Change Rate (LCR):** number of lead changes per 100 laps.

---

## Run locally (optional)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app/streamlit_app.py
