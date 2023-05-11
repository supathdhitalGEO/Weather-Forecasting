# Weather Forecasting
We aim to forecast precipitation and temperature for next 2 to 3 hours by using the past meteorological staion data with different parameter like Humidity,
Minimum , maximum Temperature, Precipitation, wind speed etc. In context of Nepal, Numerical Weather Forecasting is adopted which needs high processing PC along with long computational
time so this raises so many problems in Agriculture, Flood ans so on. In this Project it contains the raw data, data cleaning, exploratory data analysis,
ML modeling( we will use LSTM).It will contains different folders associated with different tasks.

# 1.1 Introduction
Weather can be introduced as a persistent, multidimensional, data-intensive and dynamic process that indicates the state of air on the earth at a particular time and place. Weather forecasting, the prediction of the condition of the atmosphere for a given location and time through the application of the principles of physics, has been one of the most technologically and scientifically complicated issues faced worldwide today. Early Numerical Weather Prediction (NWP) based weather forecasting, has been somehow replaced by Artificial Intelligence (AI) techniques these days.


# All Station Data
It contains the data of all satation cleaned data in an organized form.It can be used for the modeling. These data are free from outliers and the NaN values so, these data are used to forecast the weather.

# Model
It contains all the files of modeling using the Long Short Term Memory(LSTM). Our model will forecast the weather for next two hours for Pokhara airport station and rest of the data will forecasted daily. 


Till now we have got an accuracy of 60% for the precipitation pattern to forecast precipitation value and 86% for the temperature data.

# Weather Portal
All the predictions and the precipitaion trends are overviewed through the web application where we will show the prediction value of all stations with the last certain days graph trends. This portal will work on the basis of the model that we developed and the database of  out dataset.
