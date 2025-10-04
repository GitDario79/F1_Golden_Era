import pandas as pd
from src.metrics import _race_pvi, _race_lcr

def test_metrics_nonnegative():
    df = pd.DataFrame({
        "driverId":[1,1,1,2,2,2],
        "lap":[1,2,3,1,2,3],
        "position":[1,2,1,5,4,3],
        "leader":[1,1,1,1,1,1]
    })
    assert _race_pvi(df[["driverId","lap","position"]]) >= 0
    assert _race_lcr(df[["lap","leader"]]) >= 0
