# Data-Driven Analysis of Road Accidents in India

## Project Overview

Road accidents are one of the leading causes of injuries and fatalities in India. This project performs a data-driven analysis of road accident data to identify patterns, risk factors, and accident severity trends.

Using Python and machine learning techniques, the project analyzes accident data to understand the influence of factors such as driver age, road conditions, weather, and speed limits. The study also builds predictive models to classify accident severity and provide insights that can support road safety planning.

---

## Dataset

The dataset used in this project was obtained from publicly available accident records on Kaggle. It contains detailed information about road accidents including location, environmental conditions, and accident severity.

Important features in the dataset include:

* Accident index (unique accident identifier)
* Accident severity
* Date and time of accident
* Day of the week
* Urban or rural area
* Speed limit
* Weather conditions
* Road surface conditions
* Age of driver
* Vehicle type
* Number of casualties
* Number of vehicles involved
* Road type
* Geographic location coordinates

The dataset spans multiple years of accident records, allowing meaningful analysis of accident patterns and severity.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)

---

## Data Preprocessing

Several preprocessing steps were performed to prepare the dataset for analysis:

* Handling missing values
* Removing duplicate records
* Converting date columns into datetime format
* Removing unnecessary identifier columns
* Encoding categorical variables using one-hot encoding
* Handling class imbalance using SMOTE
* Preparing data for machine learning models

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was conducted to understand accident patterns and trends.

The analysis included:

* Distribution of driver age
* Distribution of speed limits
* Number of casualties per accident
* Accident severity distribution
* Relationship between driver age and accident severity
* Accident occurrence across different days of the week

Various visualizations such as bar charts, histograms, heatmaps, line plots, and strip plots were used to explore the dataset.

---

## Machine Learning Models

Two machine learning models were implemented to predict accident severity.

### Random Forest Classifier

Random Forest is an ensemble learning method used for classification tasks.
The model achieved an accuracy of approximately 94%.

### XGBoost Classifier

XGBoost is an advanced gradient boosting algorithm that improves predictive performance.
The model achieved an accuracy of approximately 99%.

SMOTE was applied to handle class imbalance and improve prediction performance for minority classes.

---

## Model Evaluation

The models were evaluated using the following metrics:

* Confusion Matrix
* Precision
* Recall
* F1 Score
* Classification Report

The evaluation results showed that the XGBoost model performed better than the Random Forest model in predicting accident severity.

---

## Key Findings

The analysis revealed several important insights:

* Most accidents involve drivers between the ages of 20 and 50.
* The majority of accidents occur at 30 mph speed limits, indicating urban road conditions.
* Most accidents fall under the "Slight" severity category.
* Serious and fatal accidents occur less frequently but remain significant for road safety planning.

---

## Limitations

Some limitations of this project include:

* The dataset contained highly imbalanced severity classes.
* Certain important factors such as traffic density and driver behavior were not available.
* Seasonal and long-term temporal patterns were not deeply analyzed.

---

## Future Scope

The project can be extended further by:

* Using deep learning models such as LSTM or GRU for time-based prediction.
* Integrating weather, traffic, and road infrastructure data.
* Developing a real-time accident prediction system.
* Creating an interactive dashboard for accident monitoring and analysis.
