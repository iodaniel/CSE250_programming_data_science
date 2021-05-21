# %%
import numpy as np
import pandas as pd
import altair as alt
from scipy import stats
import json
import urllib3
# %%
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)
# %% #print a 
print((flights
    .tail(5)
    .filter(['year','month','airport_code'])
    .to_markdown()))
# %%
flights.describe()
# %%
flights.describe(exclude=np.number)

# %%
# %%
import pandas as pd 
import numpy as np
import altair as alt
import urllib3
import json
# %%
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)
# %%
# see markdown table
print((flights
    .tail(5)
    .filter(["year", "month", "airport_code"])
    .to_markdown()))
# %%
# figure out .describe
flights.describe()
flights.describe(exclude=np.number)
# %%
# -999 for missing num_of_delays_late_aircraft, minutes_delayed_nas
# airport_name is missing some, month is missing, 
# num_of_delays_carrier should be numeric having a problem with 1500+
pd.crosstab(flights.month, flights.year)
# %%
pd.crosstab(flights.airport_code, flights.airport_name, dropna=False)
# %%
flights.year.isnull().sum()
# %%
# maybe this is helpful
pd.crosstab(flights.year.isnull(), flights.minutes_delayed_carrier.isnull())
# %%
# Grand question 3
# According to the BTS website the Weather category only accounts for severe weather delays. 
# 
#Other "mild" weather delays are included as part of the NAS category and the Late-Arriving Aircraft category. 
#Calculate the total number of flights delayed by weather (either severe or mild) using these two rules:
# - 30% of all delayed flights in the Late-Arriving category are due to weather.
# - From April to August, 40% of delayed flights in the NAS category are due to weather. The rest of the months, the proportion rises to 65%.
# - num_of_delays_weather
# - num_of_flights_total
# - num_of_delays_late_aircraft
# - num_of_delays_nas
# - airport_code 
# missing month n/a will be multiplied by .65 assumption
weather = flights.assign(
    severe = lambda x: x.num_of_delays_weather,
    nodla_nona = lambda x: x.num_of_delays_late_aircraft.replace(-999, np.nan),
    mild_late = lambda x: x.nodla_nona.fillna(x.nodla_nona.mean())*0.30,
    mild = lambda x: np.where(x.month.isin(["April", "May", "June", "July", "August"]), 
     x.num_of_delays_nas*0.4, 
     x.num_of_delays_nas*0.65
        ),#,
    #weather = # add up stuff
    percent_weather = lambda x: 100* x.num_of_delays_weather/ x.num_of_delays_total
    )
# %%
weather.filter(['airport_code','month','severe','mild', 'mild_late',
    'weather', 'num_of_delays_total', 'percent_weather'])
    
# %%
