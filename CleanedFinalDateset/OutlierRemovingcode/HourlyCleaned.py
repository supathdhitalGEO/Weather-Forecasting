import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates


# loading the data:
data=pd.read_csv("Hourlyupdated.csv")
data.head()

#checking the null values
data.isnull().sum()

#about data
data.describe()

#changing the format of the date

# convert the date column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d %H:%M')

# change the format of the date column to "YYYY-MM-DD"
data['Date'] = data['Date'].dt.strftime("%Y-%m-%d %H:%M")

data.set_index('Date', inplace=True)
data.head()#its all set that the time column is index now

#plotting the line plot to see the trend of air temperature
temAir=data['Air Temperature']
plt.figure(figsize=(15,4), dpi=200)
plt.plot(data.index,temAir)
plt.xlabel('Dates')
plt.ylabel('Air Temperature Value')
plt.title('Line plot of Temperature Distribution')
plt.show()


#certain range only

# filter the data to the desired range
start_date = '2020-01-01 06:00'
end_date = '2020-12-31 06:00'
df_range = temAir.loc[start_date:end_date]
plt.plot(df_range.index, temAir[:8761])

# show the plot
plt.show()



#plotting a boxplot to see outlier in dataframe
data.boxplot()
plt.xticks(rotation=35)
plt.show()

#removing the outlier from certain range and replacing the data as perscribed by the Box-Plot of precipitaiton column:
# from the boxplot we can say that we can remove the data more than 45 for precipitation and less than
#30 for humidity can be taken as outlier now:
    
data['Precipitation'] = data['Precipitation'].where(data['Precipitation'] <= 45, 45)
data['Relative Humidity']= data['Relative Humidity'].where(data['Relative Humidity']>=30,30)
data['Wind Speed ']= data['Wind Speed '].where(data['Wind Speed ']<=8,8)

#now plotting the boxplot again with new updated dataframe;
data.boxplot()
plt.xticks(rotation=35)
plt.show()

#exporting the updated new dataframe
data.to_csv('Airportfinaldata.csv')    






















