# %% 
import sys
import pandas as pd
import numpy as np 
import altair as alt
# %%
alt.data_transformers.enable('json')
# %%
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
data = pd.read_csv(url)
# %%
data.head(5).T
# %%
pd.unique(data.name).size
#len(pd.unique(data.name))
# %%
data.shape
# %%
data.query('name =="Daniel"').year.size
# %%
#data.query('name =="John"').year.size
#to request search for a name 
# %%
my_name= data.query('year' and 'name=="Daniel"')
my_name
# %%
# Grand question #1
# %% 
my_dataName = (my_name.groupby(['name', 'year'])
            .agg(Total_all = ('Total', np.sum),
                Average_all = ("Total", np.mean))
            .reset_index()
            .query("Total_all > 0")
            .sort_values('Total_all'))

print(my_dataName.head(1).name)
my_dataName.tail(1).name
# %% 
my_dataName
# %%
chart_name = (alt.Chart(my_dataName).mark_bar(
    color='red',
    opacity=0.5)
    .encode(
        x= alt.X("year", sort='-y'), 
        y="Total_all")
    ).properties(
        title="Daniel Historial Records"
    )
chart_name.configure_title(
    fontSize=20,
    font="Conrier",
    color='blue',
    anchor='start'
)
chart_name
# %%
chart_loess = (alt.Chart(my_dataName)
  .encode(
    x = "year",
    y = "Total_all")
  .transform_loess("year", "Total_all")
  .mark_line()
)
# %%
chart = chart_name + chart_loess
chart
# %%
chart.save("screenshot/record_name.png")

#data_name.info()
# %%
#(alt.Chart(data_name.head(25))
#    .encode(
#        x = alt.X('year==1984', sort='-y'), 
#        y = 'name=="Daniel"')
#    .mark_line())
#which name is give the most in the list 
#agrupar un nuevo dataframe y agruparlos ------
#agg 
# %%
dataName = (data.groupby(['name'])
            .agg(Total_all = ('Total', np.sum),
                Average_all = ("Total", np.mean))
            .reset_index())
dataName

dataName.sort_values('Total_all').head(1).name
dataName.sort_values('Total_all').tail(1).name
#create a new dataframe only of name and total
# %% 
#data.sort_values('name=="Daniel"')
# %%
dataName_state = (data.groupby(['name'])
            .agg(Total_all = ('TX', np.sum),
                Average_all = ("TX", np.mean))
            .reset_index()
            .query("Total_all > 0")
            .sort_values('Total_all'))

print(dataName_state.head(1).name)
dataName_state.tail(1).name
# %%
dataName
# %%


# %%
(alt.Chart(dataName_state.head(25))
    .encode(
        x = alt.X('name', sort='-y'), 
        y = "Total_all")
    .mark_bar())
# %%

(alt.Chart(dataName.head(25))
    .encode(
        x = alt.X('name', sort='-y'), 
        y = "Total_all")
    .mark_bar())
# %%
(alt.Chart(dataName.head(25))
    .encode(
        x = alt.X('name', sort='-y'), 
        y = "Total_all")
    .mark_line())

# %%
guess_name= data.query('year' and 'name=="Brittany"')
guess_name
# %%
guessName = (guess_name.groupby(['name', 'year'])
            .agg(Total_all = ('Total', np.sum),
                Average_all = ("Total", np.mean))
            .reset_index()
            .query("Total_all > 0")
            .sort_values('Total_all'))


print(guessName.head(1).name)
guessName.tail(1).name
# %%
chart_guess = (alt.Chart(guessName).mark_bar(
    color='green',
    opacity=0.5)
    .encode(
        x= alt.X("year", sort='-y'), 
        y="Total_all")
    ).properties(
        title="Brittany Historial Records"
    )
chart_guess.configure_title(
    fontSize=20,
    font="Conrier",
    color='blue',
    anchor='start'
)
chart_guess
# %%
chart_guess.save('screenshot/guess.png')
# %%
#Grand Question 3