# %%
import pandas as pd 
import altair as alt 
import numpy as np
import urllib3 
import json
#import libraries
# %%
url_cars = "https://github.com/byuidatascience/data4missing/raw/master/data-raw/mtcars_missing/mtcars_missing.json"
cars = pd.read_json(url_cars)
url_flights = 'https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json'
http = urllib3.PoolManager()
response = http.request('GET', url_flights)
flights_json = json.loads(response.data.decode('utf-8'))
flights = pd.json_normalize(flights_json)
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman', np.nan],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip',np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT, pd.NaT],
                    "power": [np.nan, np.nan, np.nan, np.nan]})
# %% 
df
# %% %%
df.describes()
# %%
df.dropna() # this code drop all the column and rows

# %%
df.dropna(how="all")
# %%
df.dropna(how="all", axis=1)
# %%
df.dropna(how="all").dropna(how="all", axis=1) #union of the last two code_size
# %%
cars.isnull().sum()
# %%
cars.fillna(cars.mean())
# %%
cars.isnull()
# %%
cars.wt.fillna(cars.wt.mean())#fillna is a method to fill the missing data with a mean 
# %%
# %% 
print(cars)
# %% 
cars.describe()
# %%
cars.isnull().sum().sum()
# cars2 = cars
cars2 = cars.assign(
    wt2 = lambda x: x.wt.fillna(x.wt.mean()), # missing issues
    gear2 = lambda x: x.gear.replace(999, x.gear.median()) #missing issues
)
print(cars2)
# %%
cars2.isnull()
# %%
cars2.isnull().sum()
# %%
df.isnull().values.any()
# %%
cars2.wt.fillna(cars2.wt.mean(), inplace=True)
# %%
cars.gear.replace(999, cars.gear.median())

# %%
cars.isnull().sum().sum()
# %%
s = pd.Series([0, 1, np.nan, 3])
s2 = pd.Series([0, 1, np.nan, 3, np.nan, 8, np.nan, 6])
# %%
s
# %%
s2
# %%
s.interpolate() # add a number to a missing value in base of the current number 

# %%
s2.interpolate() # give you the media a+b/2
# %%
s2.ffill() #este metodo lo llena con el numero previo 

# %%
# How to check for  patterns in missing months.
pd.crosstab(flights.month, flights.year)
# %%
#crossstab is a way to match two or more column. 
pd.crosstab(flights.month, flights.airport_code)
# %%
flights.month.value_counts()#count the values in a chart

# %%
#this code print the airport_name and the count values. 
flights.airport_name.value_counts()
# %%
flights.airport_name
# %%
flights.airport_code.value_counts()
# %%

# %%
