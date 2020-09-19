## Selected Topic
Airline flight delays in 2015.

# Reason for selection
The airline industry is close to $900 billion in size worldwide as of 2019, with flight delays costing the industry $8 billion annually. Being able to predict which factors influence delays and by how many minutes, is the question airlines have been struggling to answer since their inception.

## Description of source data
This dataset provides information on the flights in 2015. Data includes the date of the flight, the airline, flight and tail number, the origin and destination airport, the times and distance associated with the flights as well as the reason for delay and if the flight was cancelled or diverted. With 31 columns and so much data, we will remove certain columns to clean the dataset. Those columns include the year because all this data is only for 2015. We will also remove the cancellation reason column because 98% of the values are null. As well, we will remove all the flights that were cancelled as it does not provide us with any data on factors that could’ve influence delay and we will remove the whole cancelled column as well.

 
## Below is the Pandas project files and folders description as of Segment-2:-

1)	Database: Data base folder has 3 files in it :-

  a.	Database.ipynb : Though this file, connected to Database to create new flight database using postgres. 
  b.	Schema.png : This is the ERD that shows the relationship among Flights, Airlines and Airports table.
  c.	Schema.txt : ERD text file

2)	Flight Delay Predictor: This is the PPT for our project eliciting the problem that we are trying to solve through our analysis, steps taken, tool used and machine learning model used.

3)	Readme.md : This file has the high-level information and flow of the project.

4)	Data_Cleaning _Final: In this file, data cleansing and exploration analysis is completed for the project analysis.

5)	ML_1.0: This file has the machine learning model used for the analysis.

6)	Source_data.txt: This file contains the link for the original data source from Kaggle.




## Question 
Which factors influence flight delays, and by how many minutes? 

# Technologies Used
## Data Cleaning and Analysis
Pandas will be used to create a DataFrame, clean the data, and perform exploratory analysis. Additional analysis will be completed using Python.

## Database Storage
Postgres is the database we intend to use, and we will use pgAdmin to display the data. 

## Machine Learning

### Data Preprocessing and Feature Engineering
The initial data file was explored and cleaning using python and pandas. As we are interested in departure and arrival delays, all rows with cancelled or diverted flights were removed. The remaining delay times had a low varience and normal distribution centered around 0, with a weak right skew stretching from 200 minuts to 1700 minuits. The large delays are caused by factors outside the airlines control, and rows with delays over 120 minuits were dropped. Of the columns present in the data set, multiple columns were made up of a linear combination of other columns. The redundant columns were dropped removing linear relationships between columns. The remaining data consisted of 23 columns, and 3,292,910 rows. 
The categorical data was encoded using a dictionary to replace stings with integers. The dictionary and replace method was chosen because it allows us to later create an interactive tool where airports/airlines can be input, and we will be able to use the dictionary to convert them to integers when passing to the ml model. These categorical columns were then encoded using sklearn OneHotEncoder. 

### Machine learning model
Due to the size of the data and memory limitations, the data was read in chunks. Each chunk was split into training and testing sets of 80% and 20% respectively, using sklearn train_test_split. This data was used to train, or continue trainging after the first chunk, and test our model with each chunk itteration.
Tensor flow Keras' sequential model was used to create a deep neural net (DNN). This was chosen becasue DNN's perform well with large amounts of data, have the ability to learn and model non-linear and complex relatonships, perform well with high volatility and non-constant variance, and has superior prediction power to other regression models. 
Our model was tuned using hyper parameter testing on the number of neurons in each hidden level, and activation functions. Overfitting was prevented by hyper parameter tuning the number of epochs. 


## Dashboard
Dash will be used to visualize our results and create a story answering our question. 

# Pandas - Communication Protocol

- Master branch- A master branch called Pandas is created for our final team work to be pushed every week.

- Under Master branch- A branch is created for each team member.

- All team members are invited as a contributor to the Pandas repository.

- Each team member will add their work to the assigned branch and one team member will push the work done by all the team members to the master branch.

- One team member will submit the link for the master branch for grading on behalf of all team members.
