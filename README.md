# Airline Flight Delays

We decided to base our project on flight delays in 2015.

# Reason for selection
The airline industry is close to $900 billion in size worldwide as of 2019, with flight delays costing the industry $8 billion annually. Being able to predict which factors influence delays and by how many minutes, is the question airlines have been struggling to answer since their inception.

## Description of source data
Our data was obtained from [Kaggle](https://www.kaggle.com/usdot/flight-delays)

This dataset provides information on the flights in 2015. Data includes the date of the flight, the airline, flight and tail number, the origin and destination airport, the times and distance associated with the flights as well as the reason for delay and if the flight was cancelled or diverted. With 31 columns and so much data, we will remove certain columns to clean the dataset. Those columns include the year because all this data is only for 2015. We will also remove the cancellation reason column because 98% of the values are null. As well, we will remove all the flights that were cancelled as it does not provide us with any data on factors that could’ve influence delay and we will remove the whole cancelled column as well.

## Question 
Which factors influence flight delays, and by how many minutes? 

# Technologies Used
## Data Cleaning and Analysis
Pandas will be used to create a DataFrame, clean the data, and perform exploratory analysis. Additional analysis will be completed using Python.

## Database Storage
We used Postgres to store the data. We accessed and manipulated the database using Python through Jupyter Notebook. 

## Machine Learning

### Data Preprocessing and Feature Engineering
The initial data file was explored and cleaning using python and pandas. As we are interested in departure and arrival delays, all rows with cancelled or diverted flights were removed. The remaining delay times had a low varience and normal distribution centered around 0, with a weak right skew stretching from 200 minuts to 1700 minuits. The large delays are caused by factors outside the airlines control, and rows with delays over 120 minuits were dropped. Of the columns present in the data set, multiple columns were made up of a linear combination of other columns. The redundant columns were dropped removing linear relationships between columns. The remaining data consisted of 23 columns, and 3,292,910 rows. 
The categorical data was encoded using a dictionary to replace stings with integers. The dictionary and replace method was chosen because it allows us to later create an interactive tool where airports/airlines can be input, and we will be able to use the dictionary to convert them to integers when passing to the ml model. These categorical columns were then encoded using sklearn OneHotEncoder. 

### Machine learning model
Due to the size of the data and memory limitations, the data was read in chunks. Each chunk was split into training and testing sets of 80% and 20% respectively, using sklearn train_test_split. This data was used to train, or continue trainging after the first chunk, and test our model with each chunk itteration.
Tensor flow Keras' sequential model was used to create a deep neural net (DNN). This was chosen becasue DNN's perform well with large amounts of data, have the ability to learn and model non-linear and complex relatonships, perform well with high volatility and non-constant variance, and has superior prediction power to other regression models. 
Our model was tuned using hyper parameter testing on the number of neurons in each hidden level, and activation functions. Overfitting was prevented by hyper parameter tuning the number of epochs. 

#### Accuracy
We used a regression model for our machine learning, which uses the mean squared error (MSE), and coefficient of determination (R squared) value for accuracy instead of the confusion matrix used by classification algorithms. 
The departure and arrival delay times currently have a mean squared error of approximately 155, and an average error of 12.25 minutes. This error is fairly good considering the range of arrival and departure delays as well as the variance within the data. The arrival delay predictions have an R squared of .56, which is acceptable but not great. Overall the arrival delays are represented correctly by our model 56% of the time. The departure delay had a much smaller R squarred value, and the data we had was not successful in predicting departure delays. To improve this, the variance in the data set would have to be reduced, and separate models can be trained for each individual airport, instead of having airport as a feature. 


## Dashboard
Dash was used to visualise our findings. A preview of our dashboard is displayed here
![dash_preview](https://github.com/Pandas-UFT/Pandas/blob/master/figures/dash_preview.png?raw=true)

and the functional dashboard is deployed and available here on [Heroku](https://pandas-flight-dashboard.herokuapp.com/).

A quick video of the dashboard is also available for download [here](https://github.com/Pandas-UFT/Pandas/blob/master/dashboard/dashboard.mp4) on github.

## Google Slide Deck Link

Our presentation is available [here](https://docs.google.com/presentation/d/1lVltMy94bXFktCDCRaQnMVSpEe5rUilISrqvT9a1mas/edit?usp=sharing).

## File Navigation

* dashboard: dashboard folder
  * readme.md: describes and depicts dashboard
  * app.py: our dashboard app built using Plotly's Dash framework
  * dashboard.mp4: a downloadable video showing our dashboard's features

* database: database folder
  * database.ipynb: This file connects to postgres to create the flights database
  * schema.png: This is the Entity Relationship Diagram (ERD) that shows the relationship among the Flights, Airlines and Airports tables
  * schema.txt: text file that can be used to create the ERD

* figures: folder of data visualizations
  * readme.md: Describes and displays data visualizations
  * airline_arrival_delay.png
  * airline_departure_delay.png
  * arrival_predictions.png
  * correlation_matrix.PNG
  * dash_preview.png
  * dashboard.png
  * departure_predictions.png
  * month_arrival_delay.png
  * month_departure_delay.png
  * prediction_forest_plot.PNG
  * prediction_plot.PNG
  * time_arrival_delay.png
  * time_departure_delay.png

* machine_learning: Machine Learning folder
  * checkpoints: checkpoints folder
  * hyper_parameter_tuning.ipynb: Oulines changes made to the machine learning model to improve accuracy
  * ml_arrival_delay.ipynb: Machine learning model for arrival delays
  * ml_departure_delay.ipynb: Machine learning model for departude delays

* resources: Resource folder wherein data files were stored on local machines
  * flights_complete_sample.csv: data source for building the dashboard to accomodate Heroku's deployment size limits

* .gitignore

* README.md: High-level information and flow of the project

* data_cleaning_file.ipynb: Data cleaning and exploration analysis is completed for the project analysis

* data_vis.ipynb: Code for creating all data visualizations

* flight_delay_predictor.ppt: PPT file eliciting the problem that we are trying to solve through our analysis, steps taken, tools used and machine learning model used

* requirements.txt: A list of all the technologies needed to run the analysis
