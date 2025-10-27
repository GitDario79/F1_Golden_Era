import pandas as pd

def load_results(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['wins'] = (df['position'] == 1).astype(int)
    return df

def filter_years(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    return df[(df['season'] >= start) & (df['season'] <= end)].copy()

def driver_points(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby(['season','driver'], as_index=False)['points']
              .sum()
              .sort_values(['season','points'], ascending=[True, False]))

def total_wins(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby('driver', as_index=False)['wins']
              .sum()
              .sort_values('wins', ascending=False))
