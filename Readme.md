# F1 Golden Era – Quantifying “Action” in Formula 1

Two metrics—**Position Volatility Index (PVI)** and **Lead-Change Rate (LCR)**—score how “action-packed” a season is.

## Run locally (optional)
```bash
python -m venv .venv && source .venv/bin/activate   # on Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/streamlit_app.py

CSV columns required: season, raceId, lap, driverId, position, leader

