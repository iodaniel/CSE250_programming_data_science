# %%
import sys
import pandas as pd
import altair as alt
import numpy as np
#import tables
#import tabulate as tab
# %%
alt.data_transformers.enable('json')

# %%
#extract dataframe
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)
# %%
#
mpg.head()
# %%
#shape the dataframe
mpg.shape
# %%
chart_color = (alt.Chart(mpg)#mpg dataframe called. 
  .encode(#encoder attribute
    x='displ', #variable for x value 
    y='hwy', # variable for y value 
    color ="class" 
    )
  .mark_circle()#mark_circle attribute to create circle chart.
)
chart_color
# %% 
chart_color.save("screenshot/altair_color.png")
#call the variable with save() attribute in the filea assignated.

# %%
