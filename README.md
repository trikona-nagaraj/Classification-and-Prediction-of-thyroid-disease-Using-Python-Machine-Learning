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

### Results 📈

The results revealed that the XG-Boost model exhibited superior performance with an average AUC score of 0.98, signifying its robustness in predicting hypothyroidism. Both Random Forest and K-Nearest Neighbors models displayed commendable performance with average AUC scores of 0.91 and 0.92, respectively. The model predictions were generated in the form of a CSV file.

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
