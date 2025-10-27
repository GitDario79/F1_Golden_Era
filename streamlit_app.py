import streamlit as st
import plotly.express as px
from pathlib import Path
from src.utils import load_results, filter_years, driver_points, total_wins

st.set_page_config(page_title='F1 Golden Era', page_icon='🏁', layout='wide')

# Resolve the CSV path relative to this file so the app works no matter where it's launched from
APP_DIR = Path(__file__).resolve().parent
DATA_PATH = (APP_DIR / 'data' / 'sample_results.csv')

@st.cache_data
def get_data(path: Path):
    return load_results(str(path))

st.title('🏁 F1 Golden Era — Mini Analytics')
st.markdown('A tiny, reproducible demo with sample data. Swap in your full dataset later.')

# Load data with guardrails
if not DATA_PATH.exists():
    st.error(f"Data file not found: {DATA_PATH}. Make sure 'data/sample_results.csv' exists in the repo.")
    st.stop()

df = get_data(DATA_PATH)

# Sidebar controls
years = sorted(df['season'].unique())
start, end = st.sidebar.select_slider('Season range', options=years, value=(min(years), max(years)))
top_n = st.sidebar.slider('Top drivers to display', 3, 10, 5)

# Filter
df_filt = filter_years(df, start, end)

# Points by season/driver
pts = driver_points(df_filt)
top_drivers = pts.groupby('driver')['points'].sum().sort_values(ascending=False).head(top_n).index.tolist()
pts_top = pts[pts['driver'].isin(top_drivers)]

# Chart 1: Points per season (line)
st.subheader('Points by Season — Top Drivers')
fig1 = px.line(pts_top, x='season', y='points', color='driver', markers=True)
fig1.update_layout(legend_title_text='Driver', xaxis_title='Season', yaxis_title='Points')
st.plotly_chart(fig1, use_container_width=True)

# Chart 2: Total wins (bar)
wins = total_wins(df_filt)
wins_top = wins[wins['driver'].isin(top_drivers)]
st.subheader('Total Wins — Selected Range')
fig2 = px.bar(wins_top, x='driver', y='wins', text='wins')
fig2.update_layout(xaxis_title='Driver', yaxis_title='Wins')
st.plotly_chart(fig2, use_container_width=True)

# Table: current slice
st.subheader('Current Slice (sample)')
st.dataframe(df_filt.head(20), use_container_width=True)

st.caption('Data: tiny handcrafted sample for demo. Replace data/sample_results.csv with your full dataset to scale up.')
