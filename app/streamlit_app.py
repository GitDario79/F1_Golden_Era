# Standard imports at the very top (Ruff happy)
import sys
from pathlib import Path
import streamlit as st
import pandas as pd

# Add repo root to sys.path so "src" is importable when running from app/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.metrics import season_summary  # noqa: E402

st.set_page_config(page_title="F1 Golden Era", layout="wide")
st.title("F1 Golden Era – Action Index (MVP)")

st.write("Upload a CSV with columns: season, raceId, lap, driverId, position, leader")

file = st.file_uploader("Upload race laps CSV", type=["csv"])
if file:
    df = pd.read_csv(file)
    seasons = sorted(df["season"].unique())
    season = st.selectbox("Season", seasons, index=len(seasons)-1)
    res = season_summary(df, season)
    st.subheader(f"Season {season} summary")
    col1, col2 = st.columns(2)
    col1.metric("PVI (mean per race)", f"{res['pvi_mean']:.2f}")
    col2.metric("Lead-change rate (per 100 laps)", f"{res['lcr_mean_per100']:.2f}")
    st.write("Race-level table")
    st.dataframe(res["by_race"])
else:
    st.info("Waiting for CSV...")
