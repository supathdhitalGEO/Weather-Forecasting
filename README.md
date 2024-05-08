
We aim to forecast precipitation and temperature for the next 2 to 3 hours by using past meteorological station data with different parameters like Humidity,
Minimum, maximum Temperature, Precipitation, wind speed, etc. In the context of Nepal, Numerical Weather Forecasting is adopted, which requires a high-processing PC along with long computational
time so this raises so many problems in Agriculture, floods, and so on.

It will contain different folders associated with different tasks.
# LSTMModels and Dataset
The LSTM models for forecasting the air temperature and precipitation at different stations are within this folder. All the models are mentioned in the naming convention itself (e.g., to run the airport, hourly precipitation model, there is a model with the name AirportHourlyPrecipitation.ipynb inside the airport station folder, indicating the station name and precipitation or temperature as a name). Download all the packages before running, and the model's data can be accessed via the CleanedFinalDataset Folder. 

The Model architecture based on the aforementioned code looks like this:
<img src="https://github.com/supathdhitalGEO/Weather-Forecasting/blob/main/visualization/images/Model_arct%20(1).jpg"/>

# Outlier Handling and Data Cleaning
This contains the sample code of the percentile approach of handling outliers and the data cleaning process of a few data frames.

# Visualization
This contains the visualization of the dataset for further analysis and action.

# Weather Portal
The final visualization of the output of models can be seen through the weather portal. The weather portal can be accessed from [Here](https://github.com/Kapil-bit/Web-portal).

# Attribution
If you use this code or dataset, cite the work as follows: <br>
For DATA: <br>

Dhital, Supath; Lamsal, Kapil; Shrestha, Sulav; Bhurtyal, Umesh (2023). Meteorological Dataset, Data Cleaning and Modeling using LSTM for Weather Prediction. figshare. 
   Dataset. [https://doi.org/10.6084/m9.figshare.23813487.v2](https://doi.org/10.6084/m9.figshare.23813487.v2) <br>
   
And, the full paper is available at [Dhital, Supath, et al.](https://doi.org/10.23918/eajse.v10i2p02). To cite this work:<br>

Dhital, S., Lamsal, K., Shrestha, S., & Bhurtyal, U. (2024) "Forecasting Weather using Deep Learning from the Meteorological Stations Data: A Study of Different Meteorological      Stations in Kaski District, Nepal", Eurasian J. Sci. Eng, 10(2), pp.16-33.[https://doi.org/10.23918/eajse.v10i2p02](https://doi.org/10.23918/eajse.v10i2p02)


