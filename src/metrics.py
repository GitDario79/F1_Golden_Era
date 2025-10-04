import pandas as pd

def _race_pvi(df_race: pd.DataFrame) -> float:
    """
    Position Volatility Index (PVI):
    mean absolute lap-to-lap position change per driver, averaged across drivers.
    Works across pandas versions (no min_count arg).
    """
    df = df_race.sort_values(["driverId", "lap"]).copy()
    df["pos_shift"] = df.groupby("driverId")["position"].diff().abs()
    # Default mean() skips NaNs; then drop remaining NaNs before overall mean
    per_driver = df.groupby("driverId")["pos_shift"].mean()
    per_driver = per_driver.dropna()
    if per_driver.empty:
        return 0.0
    return float(per_driver.mean())


def _race_lcr(df_race: pd.DataFrame) -> float:
    # leader changes per 100 laps
    df_race = df_race.sort_values("lap")
    lead_changes = (df_race["leader"].shift() != df_race["leader"]).sum() - 1
    lead_changes = max(lead_changes, 0)
    laps = df_race["lap"].nunique()
    return (lead_changes / laps) * 100 if laps else 0.0

def season_summary(df: pd.DataFrame, season: int):
    sub = df[df["season"] == season].copy()
    by_race = []
    for rid, g in sub.groupby("raceId"):
        pvi = _race_pvi(g[["driverId","lap","position"]].dropna())
        lcr = _race_lcr(g[["lap","leader"]].dropna())
        by_race.append({"raceId": rid, "pvi": pvi, "lcr_per100": lcr})
    by_race = pd.DataFrame(by_race)
    return {
        "pvi_mean": by_race["pvi"].mean(),
        "lcr_mean_per100": by_race["lcr_per100"].mean(),
        "by_race": by_race.sort_values("raceId")
    }
