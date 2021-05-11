
# %%
import pandas as pd 
import numpy as np 
import altair as alt 
# %%
url = "https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv"
dat = pd.read_csv(url)
# %%
axis = alt.Axis(format=".0f")
chart1=(alt.Chart(dat.query("name== 'David' or name== 'Daniel'"), title = "The occurance of names")
    .encode(
        alt.X("year", axis=alt.Axis(format=".0f"), title ="Year of Birth"), 
        alt.Y("Total", title = "Number of  birth names"),
        alt.Color("name")
    )
    .mark_line())
chart1
# visualizacion de dos nombres
# %%
dat_line = pd.DataFrame({
    "year":[1984, 1956],
    "name": ["Daniel", "David"],
    "label": ["David's Birth", "Daniel's Birth"],
    "y": [15000, 30000]
})
line_chart = alt.Chart(dat_line).encode(x = "year", color="name").mark_rule()
label_chart = alt.Chart(dat_line).encode(
    x = "year", 
    y = "y", 
    text = "label",
    color = "name").mark_text()
chart1 + label_chart + line_chart

# %%
(dat
    .groupby('name')
    .sum()
    .reset_index()
    .query('name=="Oliver"')
    .filter(['name', 'UT','Total'])
    .sort_values('Total'))

    # to see what is the predominant name per state and per name 
# %%
dat.shape
# %%
chart
# %%
my_name= dat.query('year' and 'name=="Daniel"')
my_name
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
chart_name = (alt.Chart(my_dataName).mark_circle(
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
