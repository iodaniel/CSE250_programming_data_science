#how to manage missing data
#mean or remove data 
#API --> Json(javascript object notation) 
#computer --> computer
#Query --> Query
# %% 
import urllib3 
import json
import pandas as pd
import numpy as np
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"

# %%
http = urllib3.PoolManager()
response = http.request('GET', url)
cars_json = json.loads(response.data.decode('utf-8'))
# %%
