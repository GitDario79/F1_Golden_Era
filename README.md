# F1 Golden Era — Quantifying “Action” in Formula 1 (1983–2021)

This project performs a data-driven analysis of historical Formula 1 data (**1983–2021**) to identify which seasons and eras featured the most “action-packed” races.

Because we don’t have a reliable **overtake count** in the dataset used here, we use **grid-to-finish position gains** as a practical proxy for race “action”.

![tests](https://img.shields.io/github/actions/workflow/status/GitDario79/F1_Golden_Era/python.yml?label=tests)
![license](https://img.shields.io/badge/license-MIT-informational)
![python](https://img.shields.io/badge/python-3.11+-blue)

---

## Core idea (the metric)

For each driver in each Grand Prix:

- `Quali_Pos` = qualifying/grid position
- `Race_Pos` = finishing position

Compute:

- `Position_Change = Quali_Pos - Race_Pos`
- `Positions_Gained = max(Position_Change, 0)`  *(only gains; position losses are clipped to 0)*

Then:

- **Race action score** = sum of `Positions_Gained` across all drivers in that race
- **Season action score** = mean race action score across races in that season


---

## What you can find in this project

### Season & era “action” ranking
- Average positions gained per race for each season
- Comparison across three sporting eras:
  - **High-Action / No Refueling (1983–1993)**
  - **Refueling Allowed (1994–2009)**
  - **Modern / No Refueling (2010–2021)**

### Driver-level analysis (1983–2021)
- **Overtake King per year:** driver with max total `Positions_Gained` in that season
- **Career overtake leaders:** drivers ranked by total `Positions_Gained` (1983–2021)
- **Overtake efficiency (ratio):** `Positions_Gained / Races_Attended` (with a minimum races filter to avoid one-off outliers)


---

## Dataset & coverage

The raw dataset (from Kaggle) contained seasons earlier than 1983, but **the analysis intentionally filters to 1983+** because qualifying/grid data is sparse or inconsistent for many earlier years.

---


