from pathlib import Path
from src.utils import load_results, filter_years, driver_points, total_wins

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_results.csv"

def test_utils_pipeline():
    df = load_results(str(DATA))
    assert {"season","driver","points","wins"}.issubset(df.columns)

    dff = filter_years(df, 1950, 1952)
    assert dff["season"].min() >= 1950 and dff["season"].max() <= 1952

    pts = driver_points(dff)
    assert {"season","driver","points"}.issubset(pts.columns)

    wins = total_wins(dff)
    assert "wins" in wins.columns and wins["wins"].ge(0).all()
