import plotly.express as px
import pandas as pd


df = pd.read_pickle('ubxPacket_20210901-165743_df.pkl')

fig = px.scatter(
    df,
    x='lon',
    y='lat',
    # color='lat'
)

fig.show()
