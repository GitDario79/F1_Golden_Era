# F1 Golden Era – Quantifying “Action” in Formula 1

![tests](https://img.shields.io/github/actions/workflow/status/GitDario79/F1_Golden_Era/python.yml?label=tests)
![license](https://img.shields.io/badge/license-MIT-informational)
![python](https://img.shields.io/badge/python-3.11+-blue)

This project performs a data-driven analysis of historical Formula 1 data (1950–2021) to quantify how “action-packed” races and eras were.  
Instead of relying on subjective impressions, it compares **qualifying grid** vs **race results** and uses lap-level metrics to score unpredictability.

> _Optional preview image goes here once you add it:_  
> ![App preview](docs/summary.png)

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

```

## Quick demo
Start the app and choose **Upload CSV**, then pick `data/sample_laps.csv`.

### Data format (for Upload mode)
CSV (or Parquet) with columns:
- `season` (int)
- `raceId` (int or string)
- `lap` (int)
- `driverId` (string)
- `position` (int; 1 = leader)
- `leader` (string; the `driverId` of the lap leader)


## Methodology (summary)
Data loading & cleaning: load/consolidate season CSVs for qualifying and race results.

Custom “Positions Gained” metric: number of positions a driver gained from start (grid) to finish; sum per race as an “action score.”

Data reliability filter: qualifying data before 1983 is sparse → analyses focus on 1983–2021.

Era-based analysis: seasons are grouped for comparison:

- **High-Action / No Refueling (1983–1993)**
- **Refueling Allowed (1994–2009)**
- **Modern / No Refueling (2010–2021)**

## Key findings (from the analysis)
1983–1993 era emerges as the most action-packed (higher positions gained per race), likely due to turbo power and lower reliability.

1994–2009 (Refueling): rule/safety changes; second most volatile by positions gained.

2010–2021 (DRS era): despite overtaking aids, results were more predictable (greater reliability/complex aero).

Driver highlight: Fernando Alonso identified as a top career overtaker by positions gained.

## Tests
```bash
pytest -q
```
## Quick links
- App UI: [`app/streamlit_app.py`](app/streamlit_app.py)
- Metrics: [`src/metrics.py`](src/metrics.py)
- Tests: [`tests/test_metrics.py`](tests/test_metrics.py)
- Sample data: [`data/sample_laps.csv`](data/sample_laps.csv)


## License
This project is released under the MIT License.



