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
#load and give a format in a chart to a json file 
# %%
flights.head()#visualize dataframe 
# %%
flights.shape# can provide the number of columns and rows of the dataframe
# %%
flights.dtypes
# %%
#review if we have any missing value 
flights.isnull().sum()
# That mean we have some missing value in the data
#  set inclurind year, minutes_delayed_carrier and 
# minutes_delater_nas

# %%
year_missing_value=flights.year.isnull().sum()
year_missing_value
# we have 23 missing values for the year, I will fill this
# missing values with ffill() method
# %%
df= flights.assign(
    year = lambda x: x.year.ffill(),
    minutes_delayed_carrier = lambda x: x.minutes_delayed_carrier.fillna(x.minutes_delayed_carrier.mean()),
    minutes_delayed_nas = lambda x: x.minutes_delayed_nas.fillna(x.minutes_delayed_nas.mean()),
)

#year = flights.year.ffill()
# %% 
df.isnull().sum()
# %%
df.head()
#verification of missing values correct new dataframa df_remove_missing_values
#year.isnull().sum()
#verification that I did not have a missing value in years. 
# %%
df.columns

# %%
df.num_of_delays_total.value_counts()
# %%
df.minutes_delayed_total.value_counts()
# %%
df.num_of_delays_total.sum()
# %%
delay = pd.crosstab(df.airport_name, df.num_of_delays_total)
#pd.crosstab(flights.month, flights.year)
print(delay)
# %%

# %%
df.dtypes
# %%
df.num_of_delays_total.sum()

# %%
df.groupby('airport_name')['num_of_delays_total'].mean()
# %%

# %%
df1=df.assign(
    minutes_delayed_total = lambda x: x.minutes_delayed_total / 60,
    proportional_delay = lambda x: (x.num_of_delays_total) / (x.num_of_flights_total)
)
df1= df1.replace('', "Washington Dulles, International Airoport") 
# %%
#table
table = pd.pivot_table(df1,  index=['month'])
        #columns=['num_of_flights_total','minutes_delayed_total'])#, aggfunc=np.mean())
table
# %%
df1
# %%
df2 =df1.groupby('airport_name')['num_of_flights_total','num_of_delays_total','minutes_delayed_total', 'proportional_delay'].sum().reset_index()
# %%
print(df2.to_markdown())
#print((df2
#    .tail(5)
#    .filter(['year','month','airport_code'])
#    .to_markdown()))
# %%
df2.info()
#%% %
df2
# %%
'''chart_guess = (alt.Chart(df2).mark_bar(
    color='green',
    opacity=0.5)
    .encode(
        x= "airport_name", 
        y="proportional_delay")
    ).properties(
        title="Month number of delays"
    )
chart_guess.configure_title(
    fontSize=20,
    font="Conrier",
    color='blue',
    anchor='start'
)
chart_guess'''
# %%
#in base of the code and de proportion the airport with more delay is Denver, CO: Denver International.
# %%
month_delay= pd.crosstab(df1.proportional_delay, df1.month)
month_delay

# %%
#crossstab i a way to match two or more column. 
pd.crosstab(df1.month, df1.airport_code)
# %%
df1.month.value_counts()#count the values in a chart

# %%
#this code print the airport_name and the count values. 
df1.airport_name.value_counts()
# %%
df1.airport_name
# %%
df1.airport_code.value_counts()
# %%
#I was determinate to drop the column n/a one is not determinant data and two is 
# not signification in relation with Size of the MUESTRA
# the 
#month_NA = df1[df1['month']=='n/a'].index
#df1.drop(month_NA, inplace=True)
# %%
#month_num = {'month':{"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}}
# %%
#obj_month = df1.replace(month_num)

# %%
df3 = df1.groupby('month')['month','proportional_delay', 'num_of_delays_total'].sum().reset_index()
df3 = df3.drop(labels=12, axis=0) #drop n/a data 
df3
# %%
df3
# %%
df.info()
# %%
chart = (alt.Chart(df3).mark_bar(
    color='blue',
    opacity=0.5)
    .encode(
        x= alt.X("month", axis=alt.Axis(), sort='-y'), 
        y="proportional_delay")
    ).properties(
        title="Delay per month"
    )
chart.configure_title(
    fontSize=20,
    font="Conrier",
    color='blue',
    anchor='start'
)
chart
#graph=alt.Chart(df3).mark_bar(extent=3.0).encode(
#    x ="month",
#    y = "proportional_delay"
#)
#graph
# %%'''
chart.save("screenshot/months.png")
'''chart_guess = (alt.Chart(df1).mark_bar(
    color='green',
    opacity=0.5)
    .encode(
        x= alt.X("month",axis=alt.Axis), 
        y="num_of_delays_total")
    ).properties(
        title="Month number of delays"
    )
chart_guess.configure_title(
    fontSize=20,
    font="Conrier",
    color='blue',
    anchor='start'
)
chart_guess'''

# %%
weather = df1.assign(
    severe = lambda x: x.num_of_delays_weather,
    nodla_nona = lambda x: x.num_of_delays_late_aircraft.replace(-999, np.nan),
    mild_late = lambda x: x.nodla_nona.fillna(x.nodla_nona.mean())*0.30,
    mild = lambda x: np.where(x.month.isin(["April", "May", "June", "July", "August"]), 
     x.num_of_delays_nas*0.4, 
     x.num_of_delays_nas*0.65
        ),#,
    weather = (lambda x: x.severe + x.mild_late + x.mild),# add up stuff
    percent_weather = lambda x: 100* x.num_of_delays_weather/ x.num_of_delays_total
    )
# %%
weather_table=weather.filter(['airport_code','month','severe','mild', 'mild_late',
                                'num_of_delays_total','num_of_weather_delays', 'weather','percent_weather'])
# %%
print(weather_table)
#df_weather = df1.groupby('month')['month','proportional_delay', 'num_of_delays_total'].sum().reset_index()
#df3
weather_grouping_month = weather.groupby('airport_code')['month','severe','mild', 'mild_late', 'num_of_delays_total', 'weather','percent_weather'].sum().reset_index()
weather_grouping_month
# %%
'''
axis = alt.Axis(format=".0f")
chart_compare=(alt.Chart(weather_grouping_month.query("'mild' or 'severe' or 'mild_late' or 'percent_weather' "), title = "The comparison between four names")
    .encode(
        alt.X("airport_code", axis=alt.Axis(format=".0f"), title ="Year of Birth"), 
        alt.Y("num_of_delays_total", title = "Number of birth names"),
        alt.Color("")
    )
    .mark_line())
chart_compare'''
# %%
