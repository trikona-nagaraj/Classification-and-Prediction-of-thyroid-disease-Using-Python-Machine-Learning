---

# Advance classification & prediction of thyroid using Python and Machine learning 🧪🔍

## Project Description

The "Advance classification & prediction of thyroid to mitigate risk of thyroid replacement in early stages" project aimed to develop a machine learning-based tool for accurately predicting the presence and severity of hypothyroidism in patients to mitigate the risk of thyroid replacement therapy.

### Objective 🎯

The objective of this project was to leverage machine learning algorithms—Random Forest, K-Nearest Neighbors, and XG-Boost—to classify patients into different hypothyroidism categories. The dataset consisted of 29 features and underwent pre-processing techniques such as missing value treatment, data transformation, and validation.

### Methodology 📊

1. **Data Preprocessing**: The dataset underwent various preprocessing steps, including missing value handling, transformation, and validation.
2. **Clustering**: Employed the KNN algorithm to cluster data into three groups.
3. **Model Building**: Utilized Random Forest, K-Nearest Neighbors, and XG-Boost algorithms to build models for each cluster.
4. **Model Evaluation**: Models were assessed using the AUC metric, with XG-Boost outperforming others with an average AUC score of 0.98.


---

## Results 📈

### Model Performance

The performance of the machine learning models was evaluated using the AUC (Area Under the Curve) metric. Here are the average AUC scores obtained:

- **XG-Boost**: 0.98 🏆
- **Random Forest**: 0.91
- **K-Nearest Neighbors**: 0.92

### Methodology

1. **Data Preprocessing**: Techniques included missing value treatment, transformation, and validation to ensure data quality and reliability.
2. **Clustering**: Utilized the KNN algorithm to segment data into three clusters based on similarity.
3. **Model Building**: Developed models for each cluster using Random Forest, K-Nearest Neighbors, and XG-Boost algorithms.
4. **Model Evaluation**: The AUC metric assessed model performance, with XG-Boost exhibiting superior accuracy compared to other models.

### Result Analysis

The XG-Boost model demonstrated remarkable accuracy in predicting the presence and severity of hypothyroidism, with an average AUC score of 0.98. This high accuracy level signifies the model's robustness in classification tasks related to thyroid conditions. 

---


### Strengths and Limitations ⚡️🛑

Strengths include modular coding, data validation, and transformation techniques ensuring result accuracy. However, limitations involve local deployment and dependency on raw data folder naming.

### Project Impact 🚀

This project holds the potential to significantly enhance thyroid disease diagnosis and treatment efficacy through data-driven predictive models.

## Application Data Input Requirements 📝

The application requires specific information from data files:
- File Names
- Length of Date and Time values
- Number of Columns
- Column Names and Datatypes

These details help maintain data uniformity and are pivotal for data matching within the application.

## Tools Employed ⚙️

The project utilized various tools for development:
- **Programming Language**: Python 🐍
- **IDE**: PyCharm 🖥️
- **Libraries**: Scikit-learn, Pandas, NumPy 📚
- **Database**: SQLite-3 💽
- **Frameworks**: Flask 🌐
- **API Testing**: Postman 📤

The combination of these tools facilitated efficient machine learning model development.

## Application Code Structure 🏗️

The application code, written in Python, follows a modular structure. The `Main.py` script houses key functions such as:
- `Train Route Client`: Initiates model training operations.
- `Predict Route Client`: Executes prediction operations.

These functions are accessible through defined routes (/train, /predict) using Flask.

## Architecture 🏛️

The project architecture comprises four key stages:
1. **Data Ingestion**
2. **Model Training**
3. **Deployment**
4. **Prediction**

Additionally, the logging module in Python records each step of code execution for reference.

---
