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



# Add repo root to sys.path so "src" is importable when running from app/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.metrics import season_summary  # noqa: E402


# -----------------------
# Helpers
# -----------------------
LAP_COLS = {"season", "raceId", "lap", "driverId", "position", "leader"}
GAINS_COLS = {"Year", "Grand Prix", "Driver", "Quali_Pos", "Race_Pos"}
RACE_ACTION_COLS = {"Year", "Grand Prix", "Race_Action_Score"}


def detect_mode(df: pd.DataFrame) -> str:
    cols = set(df.columns)
    if LAP_COLS.issubset(cols):
        return "lap"
    if GAINS_COLS.issubset(cols):
        return "gains"
    if RACE_ACTION_COLS.issubset(cols):
        return "race_action"
    return "unknown"


def ensure_positions_gained(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Quali_Pos"] = pd.to_numeric(df["Quali_Pos"], errors="coerce")
    df["Race_Pos"] = pd.to_numeric(df["Race_Pos"], errors="coerce")
    df = df.dropna(subset=["Quali_Pos", "Race_Pos"])
    df["Quali_Pos"] = df["Quali_Pos"].astype(int)
    df["Race_Pos"] = df["Race_Pos"].astype(int)

    if "Positions_Gained" not in df.columns:
        df["Positions_Gained"] = (df["Quali_Pos"] - df["Race_Pos"]).clip(lower=0)

    return df


# -----------------------
# App
# -----------------------
st.set_page_config(page_title="F1 Golden Era", layout="wide")
st.title("F1 Golden Era – Action Index (MVP)")

st.write(
    "Upload a CSV in one of these formats:\n"
    "1) Lap-level (PVI/LCR): season, raceId, lap, driverId, position, leader\n"
    "2) Grid→finish (Positions Gained): Year, Grand Prix, Driver, Quali_Pos, Race_Pos"
)

default_path = Path("data/processed/positions_gained_driver_race_1983_2021.csv")
file = st.file_uploader("Upload CSV", type=["csv"])

if file is None and default_path.exists():
    df = pd.read_csv(default_path)
    st.caption(f"Loaded default file: {default_path}")
else:
    if file is None:
        st.info("Waiting for CSV...")
        st.stop()
    df = pd.read_csv(file)

mode = detect_mode(df)

# -----------------------
# Mode: lap-level (existing behaviour)
# -----------------------
if mode == "lap":
    seasons = sorted(df["season"].dropna().unique())
    if not seasons:
        st.error("No valid seasons found in column 'season'.")
        st.stop()

    season = st.selectbox("Season", seasons, index=len(seasons) - 1)
    res = season_summary(df, season)

    st.subheader(f"Season {season} summary")
    col1, col2 = st.columns(2)
    col1.metric("PVI (mean per race)", f"{res['pvi_mean']:.2f}")
    col2.metric("Lead-change rate (per 100 laps)", f"{res['lcr_mean_per100']:.2f}")

    st.write("Race-level table")
    st.dataframe(res["by_race"], use_container_width=True)
    st.stop()

# -----------------------
# Mode: grid→finish positions gained
# -----------------------
if mode == "gains":
    df = ensure_positions_gained(df)

    years = sorted(df["Year"].dropna().unique())
    if not years:
        st.error("No valid years found in column 'Year'.")
        st.stop()

    year = st.selectbox("Year", years, index=len(years) - 1)
    dfx = df[df["Year"] == year].copy()

    # Race action score: sum of positions gained per GP
    by_race = (
        dfx.groupby(["Year", "Grand Prix"], as_index=False)["Positions_Gained"]
        .sum()
        .rename(columns={"Positions_Gained": "Race_Action_Score"})
        .sort_values("Race_Action_Score", ascending=False)
    )

    avg_action = float(by_race["Race_Action_Score"].mean()) if len(by_race) else 0.0

    st.subheader(f"{year} — Positions-Gained Action Summary")
    c1, c2, c3 = st.columns(3)
    c1.metric("Races in dataset", f"{by_race.shape[0]}")
    c2.metric("Avg action score (sum per race)", f"{avg_action:.2f}")
    c3.metric("Total positions gained (year)", f"{dfx['Positions_Gained'].sum():.0f}")

    st.write("Race-level table (sorted by action score)")
    st.dataframe(by_race, use_container_width=True)

    # Driver leaderboard
    st.write("Driver leaderboard (total positions gained)")
    by_driver = (
        dfx.groupby("Driver", as_index=False)["Positions_Gained"]
        .sum()
        .sort_values("Positions_Gained", ascending=False)
    )
    st.dataframe(by_driver.head(30), use_container_width=True)

    st.stop()

# -----------------------
# Mode: already aggregated race_action
# -----------------------
if mode == "race_action":
    years = sorted(df["Year"].dropna().unique())
    year = st.selectbox("Year", years, index=len(years) - 1)
    by_race = df[df["Year"] == year].copy()

    st.subheader(f"{year} — Race Action (pre-aggregated)")
    st.metric("Avg action score", f"{by_race['Race_Action_Score'].mean():.2f}")
    st.dataframe(by_race.sort_values("Race_Action_Score", ascending=False), use_container_width=True)
    st.stop()

# -----------------------
# Unknown schema
# -----------------------
st.error("CSV format not recognized.")
st.write("Columns found:", list(df.columns))
st.write("Expected either lap-level columns:", sorted(LAP_COLS))
st.write("…or grid→finish columns:", sorted(GAINS_COLS))
