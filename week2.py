# %%
import pandas as pd 
import numpy as np 
import altair as alt 
# %%
url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)
flights_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/flights/flights.csv"
flights = pd.read_csv(flights_url)
flights['time_hour'] = pd.to_datetime(flights.time_hour, format = "%Y-%m-%d %H:%M:%S")
df = pd.DataFrame(
{"a" : [4 ,5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]})
# %%
# Can someone read this code in english?
# %%
# sort my table by column a then
# only use the first 2 rows then
# calculate the mean of column b.
df.sort_values('a').head(2).b.mean()
# %%
# rename column a to duck then
# subset to only have duck and b columns then
# keep all rows where b is less than 9 then
# find the min of duck
mynine = 9
myresult = (df.rename(columns = {"a":"duck"})
    .filter(["duck", "b"])
    .query("b < @mynine")
    .duck
    .min())
# %%
# Altair Example
(flights
    .filter(['dep_time'])
    .assign(
      hour = lambda x: x.dep_time // 100,
      minute = lambda x: x.dep_time % 100
      ))
# %%
chart_loess = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy")
  .transform_loess("displ", "hwy")
  .mark_line()
)
chart_points = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color = "manufacturer")
  .mark_circle(size = 150)
)
# %%
chart_loess + chart_points #esto hace que se combinen dos graficos
# %%