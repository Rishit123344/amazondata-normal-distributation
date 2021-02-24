import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("amazondata.csv")
amazonlist = df["Avg Rating"]
fig = ff.create_distplot([amazonlist],['amazonresult'],show_hist = False)
fig.show()
