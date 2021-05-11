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
        x= alt.X("year", axis=alt.Axis(format=".0f"), sort='-y'), 
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
            .agg(
                Total_all = ('UT', np.sum),
                Average_all = ("UT", np.mean))
            .reset_index()
            .query("Total_all > 0")
            .sort_values('Total_all')
            )

print(dataName_state.head(1).name)
dataName_state.tail(1).name
# %%
dataName
# %%

#data.query('name =="Oliver"').year.size
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
        x= alt.X("year",axis=alt.Axis(format=".0f"), sort='-y'), 
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
#why to create a dataFrame in Pandas 
#df = pd.DataFrame({'col':[1,2],'col2':[3,4]})
# %%
#why to create a dataFrame in Pandas
#df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
#print(df)
# %%
#Grand Question 3
axis = alt.Axis(format=".0f")
chart_compare=(alt.Chart(data.query("name== 'Mary' or name== 'Martha' or name== 'Peter' or name== 'Paul'"), title = "The comparison between four names")
    .encode(
        alt.X("year", axis=alt.Axis(format=".0f"), title ="Year of Birth"), 
        alt.Y("Total", title = "Number of birth names"),
        alt.Color("name")
    )
    .mark_line())
chart_compare
# %%
data_line = pd.DataFrame({
    "year":[1920, 2000],
    'label': ["1920 compare", "2000 compare"],
    "y": [15000,52000]
})
line_chart = alt.Chart(data_line).encode(x="year").mark_rule()
label_chart = alt.Chart(data_line).encode(
    x ="year",
    y="y", 
    
    text="label").mark_text()

chart_compare_grand = chart_compare + line_chart + label_chart
# %%
chart_compare_grand.save('screenshot/name_comparison.png')
# %%
axis = alt.Axis(format=".0f")
chart_back_to_the_future=(alt.Chart(data.query("name== 'Marty' or name== 'Emmett'"), title = "Back to the Future release 1985")
    .encode(
        alt.X("year", axis=alt.Axis(format=".0f"), title ="Year of Birth"), 
        alt.Y("Total", title = "Number of birth names"),
        alt.Color("name")
    )
    .mark_line())
chart_back_to_the_future
# %%
data_line = pd.DataFrame({
    "year":[1985],
    'label': ["1985 Back to the Future Realease"],
    "y": [2500]
})
line_chart = alt.Chart(data_line).encode(x="year").mark_rule()
label_chart = alt.Chart(data_line).encode(
    x ="year",
    y="y", 
    text="label").mark_text()

chart_backToTheFuture =chart_back_to_the_future + line_chart + label_chart
# %%
chart_backToTheFuture
# %%
chart_backToTheFuture.save('screenshot/backToTheFuture.png')
# %%
axis = alt.Axis(format=".0f")
chart_ET_ext=(alt.Chart(data.query("name== 'Elliot'"), title = "1982 E.T. The extraterrestial Release")
    .encode(
        alt.X("year", axis=alt.Axis(format=".0f"), title ="Year of Birth"), 
        alt.Y("Total", title = "Number of birth names"),
        alt.Color("name")
    )
    .mark_line())
chart_ET_ext


# %%
data_line = pd.DataFrame({
    "year":[1982],
    'label': ["1982 E.T. The extraterrestial"],
    "y": [1500]
})
line_chart = alt.Chart(data_line).encode(x="year").mark_rule()
label_chart = alt.Chart(data_line).encode(
    x ="year",
    y="y", 
    text="label").mark_text()

chart_ET = chart_ET_ext + line_chart + label_chart
# %%
chart_ET
# %%
chart_ET.save('screenshot/ET.png')
# %%

# %%

# %%
