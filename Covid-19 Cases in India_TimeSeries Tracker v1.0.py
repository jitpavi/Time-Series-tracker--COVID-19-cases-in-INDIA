"""
Code Name: Time Series chart of Covid Cases in India
Code Author: Jitin Pavithran
Code Version: 1.0
Code Description: This code will generate a time-series chart to display 3 different plot of total number of Confirmed,total no.of recovered Cases and Total no. of Deaths respectively
                in India.
"""

# import all the important libraries required for this code
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import numpy as np
import requests

# Access the API which maintains the live data of the Covid-19 cases in India
ts_url = "https://api.covid19india.org/data.json"
response = requests.request("GET",ts_url)

# Convert the extracted data into a JSON object
ts_json = response.json()

#Create a dictionary and import data in JSON object
timeseries_dict = {}
for x in ts_json['cases_time_series'][0].keys():
        timeseries_dict[x] = [listitems[x] for listitems in ts_json['cases_time_series'] ]

# Import the dictionary into the Dataframe
time_series_df = pd.DataFrame(data=timeseries_dict)

# Drop the columns which are not required
time_series_df_filter = time_series_df.drop(['dailyconfirmed', 'dailydeceased', 'dailyrecovered'],axis=1)

# Replace the index column with the "date" column
time_series_df_filter.set_index(time_series_df_filter['date'],inplace=True)
time_series_df_filter.drop(labels='date',axis=1,inplace=True)

# Convert the datatype of the entire dataframe values into "int" type
time_series_df_filter[['totalconfirmed', 'totaldeceased', 'totalrecovered']] = time_series_df_filter[['totalconfirmed', 'totaldeceased', 'totalrecovered']].apply(pd.to_numeric)
time_series_df_filter.rename(columns={'totalconfirmed':'No.of Confirmed Cases', 'totaldeceased':'No.of Deaths', 'totalrecovered':'No. of Recovered Case'},inplace=True)

# Create a figure object on which the chart will be plotted
color = ['orange','red','green']
fig = plt.figure(figsize=(14,7))
plt.subplots_adjust(bottom=0.30)
plt.xticks(rotation=45, ha="right")
plt.xlabel('Date-Series',fontsize = 12)
plt.ylabel('Confirmed Cases vs Deaths vs Recovered Cases',fontsize = 12)


# Define a new function which will be used for plotting on every frame supplied bby FuncAnimation
def buildchart(i=int):
   plt.legend(time_series_df_filter.columns)
   p = plt.plot(time_series_df_filter[:i].index,time_series_df_filter[:i].values)
   plt.title(f'Time Series Visualisation of Covid-19 cases in INDIA as on {time_series_df_filter[:i].index[-1:].values}',fontsize = 12)
   for i in range(0,3):
      p[i].set_color(color[i])

#Create animator object which will accept inputs in the form figure , Function , interval and frame values
animator  = ani.FuncAnimation(fig,buildchart,interval = 1000,frames = 300,repeat=True,repeat_delay=10)

#plt.show()
#plt.close()

# Save the animator object in the form of a GIF file
animator.save(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Covid time series\Covid-19_Timeseries.gif")
