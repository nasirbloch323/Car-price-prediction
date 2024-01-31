# Data Analysis of OLX-Cars Dataset

<p align="center"><img src="https://github.com/AbdullahProjects/Car-Price-Prediction/blob/main/Money.png" width="10%" height="auto"></p>

Welcome to the project of Car Price Prediction. This project is designed to build a powerful regression who ables to predict closest prices of cars on unseen data. The [OLX Cars dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/olx-cars-dataset),is used for this project that's avaiable on Kaggle, I personally scraped it using BeautifulSoup and Requests Libraries in Python. 

## Live Demo:

See Project in Streamlit Webapp: https://akk-car-price-prediction.streamlit.app/

## About this Project:

### Motivation/Purpose:

Today, buying and selling cars online has become quite common. When someone decides to sell their car, they often wonder about the right price to ask for. For instance, if two people are selling the same car and one is asking for 20 Lac while the other is asking for 25 Lac, the person selling at 20 Lac is likely to attract more potential buyers. Similarly, when people are in the market to buy a car, they want to know the fair price for the vehicle they are interested in. That's where this project comes in – it aims to create a smart model that considers various features of a car to estimate a reasonable price. This way, both sellers and buyers can get an idea of the approximate value of a car with specific characteristics.

### Dataset I used?

[OLX Cars dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/olx-cars-dataset): Contains 9000+ records of used cars in Pakistan that owners want to sale.

### Tools:

I use following tools to develop this whole project:

- Jupyter Notebook
- Streamlit
- Pandas
- Numpy
- Scikit-Learn
- Plotly
- Pickle

### Project Development Steps:

1. **Download Dataset:** Download the dataset from Kaggle.
2. **Preprocessing:** Cleaning the dataset, Constructing new columns and Removing Unnecessary Columns.
3. **Create Model in Jupyter Notebook:** I first build model in Jupyter Notebook, then using Pickle I import model.
4. **Transform Model into Streamlit:** Pickle model imported in Streamlit for predictions.
5. **Create Streamlit Webapp:** After successfully building price prediction model, finally I create Streamlit Webapp for better user interactions.

### Learning Outcomes:

- Handle and clean dataset.
- Constructing new columns based on requirements.
- Capability to understanding dataset.
- Able to create beautiful Streamlit Webapp.
- Model Selection
- Hypermeter Tunning
- Identifying and Resolving errors from project development to deployment.
- Project Deployment
- Project Organizing
- Continous Learning


### How to Run on Your Machine

1. **Clone the Repository:** Download all files and folders from this repository.
2. **Create Virtual Environment:**
   ```bash
   py -3 -m venv virtualEnv
3. **Run this command:**
   ```bash
   pip freeze > requirements.txt
4. **Finally start the streamlit app:** Run the following command on command terminal.
   ```bash
   streamlit run streamlit_app.py
