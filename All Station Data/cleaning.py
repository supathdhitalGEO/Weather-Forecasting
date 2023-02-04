import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from datetime import datetime
import matplotlib.dates as mdates


# loading the data:
data=pd.read_csv("LamachourDaily.csv")
data.head()

#checking the null values
data.isnull().sum()

#about data
data.describe()

#changing the format of the date

# convert the date column to datetime
data['Time'] = pd.to_datetime(data['Time'], format='%d/%m/%Y %H:%M')

# change the format of the date column to "YYYY-MM-DD"
data['Time'] = data['Time'].dt.strftime("%Y-%m-%d %H:%M")

data.set_index('Time', inplace=True)
data.head()#its all set that the time column is index now

#plotting the line plot 
plt.plot(data.index, data['Precipitation(mm)'])
plt.xlabel('Dates')
plt.ylabel('Precipitaion Value')
plt.title('Line plot of Precipitation Distribution')


#certain range only

# filter the data to the desired range
start_date = '2015-01-01'
end_date = '2015-12-31'
df_range = data.loc[start_date:end_date]

# plot the precipitation values
fig, ax = plt.subplots()
ax.plot(df_range.index, df_range['Precipitation(mm)'])


# add labels and title
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.title('Precipitation Time Series Line Plot')


# show the plot
plt.show()


