import pandas as pd
from pathlib import Path

def load_historic_laps(root: str) -> pd.DataFrame:
    """
    Read per-race lap CSVs from your local folder and return ONE tidy DataFrame:
    columns: season, raceId, lap, driverId, position, leader
    - Adjust folder names and column renames below to match your files.
    - Example folder structure: <root>/<YEAR>/Race Laps/*.csv
    """
    root = Path(root)
    frames = []

    for year_dir in sorted(root.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        season = int(year_dir.name)

        # TODO: change "Race Laps" to match your actual directory
        for csv in (year_dir / "Race Laps").glob("*.csv"):
            df = pd.read_csv(csv)

            # TODO: update these rename keys to your exact headers
            df = df.rename(columns={
                "Year": "season",
                "RaceId": "raceId",
                "Lap": "lap",
                "DriverCode": "driverId",
                "Position": "position",
                "LeaderCode": "leader"
            })

            # Force correct dtypes / values if needed
            df["season"] = season
            keep = ["season", "raceId", "lap", "driverId", "position", "leader"]
            df = df[keep]
            frames.append(df)

    if not frames:
        return pd.DataFrame(columns=["season","raceId","lap","driverId","position","leader"])

    out = pd.concat(frames, ignore_index=True)
    return out.sort_values(["season","raceId","lap","driverId"]).reset_index(drop=True)
