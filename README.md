# F1_Golden_Era
This project performs a data-driven analysis of historical Formula 1 data (from 1950 to 2021) to quantitatively determine which seasons and eras featured the most "action-packed" races.
Instead of relying on subjective feelings, this analysis uses the variation between qualifying grid positions and final race results to create a metric for race unpredictability.

Quantifying “Action” in Formula 1
Two metrics—Position Volatility Index (PVI) and Lead-Change Rate (LCR)—score how “action-packed” a season is.

Run locally (optional)
python -m venv .venv && source .venv/bin/activate   # on Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app/streamlit_app.py
CSV columns required: season, raceId, lap, driverId, position, leader

## **Methodology**
**Data Loading & Cleaning:** The analysis begins by loading and consolidating dozens of individual .csv files for both qualifying and race results from each season.

**Creation of a Custom Metric:** A key metric, "Positions_Gained", was created by calculating the number of positions each driver made up from their starting grid spot to their finishing position. The total positions gained in a race served as its "action score."

**Data Reliability Filtering:** Initial exploration revealed that qualifying data prior to 1983 was sparse and unreliable. To ensure the integrity of the results, all data from before the 1983 season was filtered out of the final analysis.

**Era-Based Analysis:** The seasons from 1983 to 2021 were categorised into three distinct sporting eras to compare their average "action score":

High-Action / No Refueling (1983-1993)

Refueling Allowed (1994-2009)

Modern / No Refueling (2010-2021)

**Key Findings**
The analysis revealed a clear trend in race unpredictability over the last four decades:

The 1983-1993 era was conclusively the most action-packed, with an average of 69.2 positions gained per race, likely due to the combination of powerful turbo engines and lower mechanical reliability.

The Refuelling Era (1994-2009) started with the tragic accidents that took the lives of Ayrton Senna and Roland Ratzenberger. This period was characterised by a deep review of the rules to improve safety and reliability. It was the second most volatile period, with an average of 45.7 positions gained.

The Modern DRS Era (2010-2021), despite tools to aid overtaking, was the least volatile, with an average of 37.4 positions gained, suggesting that increased car reliability and complex aerodynamics have led to more predictable race outcomes.

Identified Fernando Alonso as the king of overtakes in Formula One history
