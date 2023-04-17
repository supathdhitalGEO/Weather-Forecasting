import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from datetime import datetime
import matplotlib.dates as mdates


# loading the data:
    
#for begnas
data=pd.read_csv("begnasupdated.csv")
data.head()

#for lumle data
data1=pd.read_csv("lumleupdated.csv")
data1.head()

#for Pokhara daily  data
data2=pd.read_csv("pokharadailyupdated.csv")
data2.head()


#checking the null values
data.isnull().sum()

#about data
data.describe()

#changing the format of the date



#for Begnas
# convert the date column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

# change the format of the date column to "YYYY-MM-DD"
data['Date'] = data['Date'].dt.strftime("%Y-%m-%d")



#For Lumle
# convert the date column to datetime
data1['Date'] = pd.to_datetime(data1['Date'], format='%Y-%m-%d')

# change the format of the date column to "YYYY-MM-DD"
data1['Date'] = data1['Date'].dt.strftime("%Y-%m-%d")




#For Pokhara Daily
# convert the date column to datetime
data2['Date'] = pd.to_datetime(data2['Date'], format='%Y-%m-%d')

# change the format of the date column to "YYYY-MM-DD"
data2['Date'] = data2['Date'].dt.strftime("%Y-%m-%d")




#For Begnas
data.set_index('Date', inplace=True)
data.head()#its all set that the time column is index now

#for Lumle
data1.set_index('Date', inplace=True)
data1.head()#its all set that the time column is index now

#For pokhara daily
data2.set_index('Date', inplace=True)
data2.head()#its all set that the time column is index now



#plotting the line plot 
plt.plot(data.index, data['Precipitaiton'])
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



#For Begnas
#plotting a boxplot to see outlier in dataframe
data.boxplot()
plt.xticks(rotation=35)
plt.show()

#For Lumle
#plotting a boxplot to see outlier in dataframe
data1.boxplot()
plt.xticks(rotation=35)
plt.show()

#For Pokhara Daily
#plotting a boxplot to see outlier in dataframe
data2.boxplot()
plt.xticks(rotation=35)
plt.show()


#For Begnas Station
#by seeing and analyzing the data the certain unusual behavior of dataframe will distract the data so 
#removing outlier we do now, by using Box plot
#precipitaion more than 130 mm is replace by 130mm, and relative humidity from 100 is replaced by 100 
#and less than 50 also removed and replace by 50
data['Precipitaiton'] = data['Precipitaiton'].where(data['Precipitaiton'] <= 130, 130)
data['Relative Humidity']= data['Relative Humidity'].where(data['Relative Humidity']>=50,50)
data['Relative Humidity']= data['Relative Humidity'].where(data['Relative Humidity']<=100,100)

#now plotting the boxplot again with new updated dataframe;
data.boxplot()
plt.xticks(rotation=35)
plt.show()



#exporting the updated new dataframe
data.to_csv('Begnasfinaldata.csv')  


#For lumle Station
#by seeing and analyzing the data the certain unusual behavior of dataframe will distract the data so 
#removing outlier we do now, by using Box plot
#precipitaion more than 170 mm is replace by 170mm,
data1['Precipitation(mm)'] = data1['Precipitation(mm)'].where(data1['Precipitation(mm)'] <= 130, 130)
data1['Relative Humidity']= data1['Relative Humidity'].where(data1['Relative Humidity']>=30,30)

#now plotting the boxplot again with new updated dataframe;
data1.boxplot()
plt.xticks(rotation=35)
plt.show()

#exporting the updated new dataframe
data1.to_csv('Lumlefinaldata.csv') 



#For pokharadaily Station
#by seeing and analyzing the data the certain unusual behavior of dataframe will distract the data so 
#removing outlier we do now, by using Box plot
#precipitaion more than 140 mm is replace by 140mm,
#and less than 30 also removed and replace by 30
data2['Precipitation'] = data2['Precipitation'].where(data2['Precipitation'] <= 140, 140)
data2['Humidity']= data2['Humidity'].where(data2['Humidity']>=30,30)


#now plotting the boxplot again with new updated dataframe;
data2.boxplot()
plt.xticks(rotation=35)
plt.show()



#exporting the updated new dataframe
data2.to_csv('Pokharadailyfinaldata.csv')  






