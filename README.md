## Multiple Disease Prediction System

This repository hosts a Multiple Disease Prediction System developed using machine learning. The system is capable of predicting three major health conditions:

🩺 Diabetes

❤️ Heart Disease

🧠 Parkinson’s Disease

## Table of Contents
- [Introduction](#Introduction)
- [key Files](#Key-Files)
- [Technologies Used](#technologies-used)
- [How It Works](#How-It-Works)
- [Requirements](#Requirements)
- [How to Run](#How-to-Run)

## Introduction 

The primary goal of this project is to provide an easy-to-use interface for individuals to assess their health risk for these conditions based on key medical parameters. 🎯🎨📊

The Healthcare Assistant is a terminal-based application that accepts inputs like age, gender, and symptoms to predict potential diseases. It uses a **Gradient Boosting Classifier** for prediction and provides probabilities for multiple possible diseases.

## Key Files

**1. heart_data.sav**

This file contains the trained machine learning model for predicting Heart Disease. The model uses parameters such as age, sex, chest pain types, resting blood pressure, cholesterol levels, and other medical readings to provide an accurate prediction. ❤️📁💻

**2. diabetes.sav**

This file includes the trained machine learning model for predicting Diabetes. It evaluates user inputs like glucose levels, insulin, BMI, age, and other health metrics to predict the likelihood of being diabetic. 🍬📁🤖

**3. parkinsons.sav**

This file holds the trained machine learning model for predicting Parkinson’s Disease. It uses specific vocal and medical attributes such as MDVP features, jitter, shimmer, and others to assess the risk of Parkinson’s. 🧠📁🎵

## Technologies Used

- **Programming Language:** Python
- **Libraries:**
  - `numpy`: For numerical operations
  - `pandas`: For data manipulation
  - `scikit-learn`: For machine learning and preprocessing
## How It Works

The main logic for the application resides in main.py. Here's an overview of its functionality:

🔄 Loading Models: The models saved in .sav files are loaded using the pickle library.

✍️ User Input: Users provide medical details through an interactive web application built with Streamlit.

🎯 Prediction: Based on the selected disease, the corresponding model predicts the outcome using the provided data.

🖥️ User Interface: The Streamlit application offers a sidebar menu for navigation and separate pages for diabetes, heart disease, and Parkinson’s predictions. 🛠️📊🔮

## Requirements

To run this application, ensure the following dependencies are installed:

✅ pandas==2.2.3

✅ numpy==2.0.2

✅ pickle-mixin==1.0.2

✅ streamlit==1.40.1

✅ streamlit-option-menu==0.4.0

✅ scikit-learn==1.5.2

Install them using the following command:

- `pip install -r requirements.txt`

📜💻✅

## How to Run

📂 Clone the repository and navigate to the project directory.

🛠️ Install the required dependencies.

🚀 Run the application using:

- `streamlit run main.py`

🌐 Access the application in your browser at http://localhost:8501. 🌐🚀📂

