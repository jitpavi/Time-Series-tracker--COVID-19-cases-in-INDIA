
# Project Name - Time-Series-tracker-of-Covid-19-cases-in-INDIA

#### -- Project Status: [Active]
Tuning the frames and interval to get the perfect animation output

## Project Intro/Objective:
Project will produce a time-series chart to display 3 different plot of total number of Confirmed,total no.of recovered Cases and Total no. of Deaths respectively in India.

### Methods Used:
* Data Exploration
* Data Wrangling
* Data Visualization

### Technologies Used:
* Python
* Pandas
* Pycharm
* Matplotlib
* FuncAnimation 

## Project Description:

### Prerequisites
  ### -> Dataset:
  * API for accessing data from the Central website hosting all the data related to cases(https://api.covid19india.org/)
  
  ### -> Python Libraries:
  * Python
  * Pandas
  * Pycharm
  * Matplotlib
  * FuncAnimation
  
### Workflow:
1. Using request module download the data using the API call from the website hosting the required data.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object.
4. Replace the index column with the Date column name "date".
5. Create a fig object where we are going to plot the chart and pass it as an input to the animator function.
6. Define a Buildchart function which will be called for every frame in plotting the chart by the FuncAnimation.
7. Create an Animator object with inputs as fig,buildchart function and interval of 30ms.
8. Save the animator object in the form of GIF format file.

## Expected Output:
 ![Covid-19_Timeseries chart](https://github.com/jitpavi/Time-Series-tracker--COVID-19-cases-in-INDIA/blob/master/Covid-19_Timeseries.gif)

## Featured Notebooks/Analysis/Deliverables
* [Covid-19 Cases in India_TimeSeries Tracker.py](https://github.com/jitpavi/Time-Series-tracker-of-Covid-19-cases-in-INDIA/blob/master/Covid-19%20Cases%20in%20India_TimeSeries%20Tracker.py)

## Versioning
Code version - v1.0

## Author:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://api.covid19india.org/

## References:

* https://towardsdatascience.com/learn-how-to-create-animated-graphs-in-python-fce780421afe
