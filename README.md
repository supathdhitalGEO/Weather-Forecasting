# Weather Forecasting
We aim to forecast precipitation and temperature for next 2 to 3 hours by using the past meteorological staion data with different parameter like Humidity,
Min/Max Temperature, Precipitation, wind speed etc. In context of Nepal, Numerical Weather Forecasting is adopted which needs high processing PC along with long computational
time so this raises so many problems in Agriculture, Flood ans so on. In this Project it contains the raw data, data cleaning, exploratory data analysis,
ML modeling( we will use LSTM).It will contains different folders associated with different tasks.

# 1.1 Introduction
Weather can be introduced as a persistent, multidimensional, data-intensive and dynamic process that indicates the state of air on the earth at a particular time and place. Weather forecasting, the prediction of the condition of the atmosphere for a given location and time through the application of the principles of physics, has been one of the most technologically and scientifically complicated issues faced worldwide today. Early Numerical Weather Prediction (NWP) based weather forecasting, has been somehow replaced by Artificial Intelligence (AI) techniques these days.

In the context of Nepal, the 72- hour based short- range weather forecasting system was initiated and since the 20th century, it has been upgraded to Numeric Weather Prediction (NWP) system. The Department of Hydrology and Meteorology (DHM) has been delivering a periodical Climate Bulletin to the public through its website. Thus, in the present scenario, Machine learning, a field of artificial intelligence based on the idea that a computer program can adapt to new data independent of human action, can be improved to enable large quantities of machine-based forecasts. With its use, weather models can better account for prediction inaccuracies and produce more accurate and reliable predictions aiding the economic and social status enhancement of Nepalese people. Accurate prediction of precipitation patterns has always been crucial in hydrological research, since it plays a key role in weather forecasting which could also serve as a promising tool to determine the early warnings of severe weather events such as  flash floods, tropical cyclones, thunderstorms, lightning, heavy rains, extreme wind or high temperature, can interrupt air and public transportation services, destroy crops or, even worse, be responsible for fatalities and injuries. Weather forecasts are also necessary for aviation, marine safety, ground traffic control, and construction industries. Forecasting precipitation is a complex process since it depends on other factors such as surface temperature (ST), humidity and pressure which are highly time dependent and vary in space. Thus, the need to build a robust mathematical model to ensure the accurate prediction of precipitation is of vital importance (Stampoulis et al.). Meteorologists produce weather forecasts by gathering as much data as possible from weather stations and then process it through the Numerical Weather Prediction model. In Nepal, weather information for the prediction model comes from surface observations provided by 337 precipitation stations, 154 hydrometric stations, 20 sediment stations, 68 climatic stations, 22 agrometeorological stations, 9 synoptic and 6 aero-synoptic stations. Meteorologists then put the observed data into a weather prediction model to create a weather forecast using supercomputers. However, making the most accurate weather predictions, particularly regarding precipitation, requires more than surface observations.
To predict complex phenomena, artificial intelligence methods have become increasingly popular. These methods are often based on machine learning algorithms, which are trained using observational data of a given phenomenon to detect it from new data. One of the most commonly employed algorithms are neural networks. As an illustration, a Convolutional Neural Network (CNN) method (Springenberg et al., 2014) was used in meteorology (Aoki, 2017) to detect and estimate rainfall using satellite images (NOAA GOES Imagery). Other examples that are more pertinent to this work include (Shi et al., 2015) and (Heye et al., 2017), which used a recurrent neural network with a long short-term memory (LSTM) to forecast rainfall using weather radar data.
A machine learning algorithm called LSTM has been used in this paper to analyze weather radar data. According to the World Meteorological Organization, nowcasting includes forecasts for the next six hours. The high spatiotemporal variability of these rainfall events makes them challenging for conventional numerical models to predict. Weather radars make it possible to track convective rainfall in real time, providing a time series of data  that can be used by the machine learning algorithm.

# 1.2 Problem Statement
Information about weather conditions is shared by DHM in Nepal based on geography like regions such as eastern, central, or western or province-by-province. As a result, it is always possible to see heavy rain within a province while other areas within the same province may not experience the same level of intensity. Hence, larger area-wise forecasts do not give an accurate result for precipitation forecasting . Weather satellites or radar can help small-area forecasts to address the lack of preparation of larger-area forecasts. Also forecast data are nonlinear and follows irregular patterns and trends, so models are required to be updated to make it fit for further use.
Meteorologists produce weather forecasts by gathering as much data as possible from weather stations and then process it through the Numerical Weather Prediction model. In Nepal, weather information for the prediction model comes from surface observations provided by 337 precipitation stations, 154 hydrometric stations, 20 sediment stations, 68 climatic stations, 22 agrometeorological stations, 9 synoptic and 6 aero-synoptic stations (DHM, n.d.). Meteorologists then put the observed data into a weather prediction model to create a weather forecast using supercomputers. However, making the most accurate weather predictions, particularly regarding precipitation, requires more than surface observations. This is where weather satellites come into account. Satellites observed precipitation over a wide range of areas unlike weather stations that record data only around it. Satellites can also detect visible and infrared atmospheric readings beyond what's possible with surface data. In addition to that, the trained Deep Learning model improves the computational time of thousands of datasets in much less time than supercomputers which perform complex mathematical equations and take hours of computation.  Hence performing the weather prediction in a rapid manner.

# 1.3 Objectives
The objective of this project is to forecast weather, more specifically precipitation and temperature using past numerical data provided by DHM. In addition to that, satellite data from Earth Observation Research Center (EORC), Japan Aerospace Exploration Agency (JAXA) is used to forecast precipitation.

   1.3.1. General Objectives
To forecast  precipitation  from weather station’s data and satellite data using deep learning.
   1.3.2. Specific Objectives
To forecast temperature using past data from weather stations.
To make the weather portal for the visualization.
# This repository contains different folders:
# Raw Data
It contains all the raw data that collected from the DHM directly.It contains several outliers and the missing values so we now have to make it frree from the outliers and missing value.

# All Station Data
It contains the data of all satation cleaned data in an organized form.It can be used for the modeling. These data are free from outliers and the NaN values so, these data are used to forecast the weather.

# Model
It contains all the files of modeling using the LSTM. Our model will forecast the weather for next two hours for Pokhara airport station and rest of the data will forecasted daily. 
