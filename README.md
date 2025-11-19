# Healthcare-Data-Analysis-Diabetes-Risk
This project analyzes a real-world healthcare dataset to understand the factors associated with diabetes risk. Using Python and Power BI, it explores key health indicators such as glucose levels, BMI, age, blood pressure, and insulin levels to uncover patterns that differentiate diabetic and non-diabetic patients.

**Objectives**

Clean and prepare medical data for accurate analysis

Explore health metrics related to diabetes

Identify patterns and risk indicators

Build clear visualizations for better interpretation

Generate insights that support early prediction and awareness

**Data Preprocessing**

The dataset contained missing and zero values for several medical attributes like:

Glucose

BMI

Blood Pressure

Skin Thickness

Insulin

These values were handled using statistical imputation to ensure reliable analysis.

**Exploratory Data Analysis (EDA)**

EDA was performed using Python (Pandas, NumPy, Seaborn, Matplotlib) to generate:

Outcome count visualization

Glucose distribution

Age vs. BMI scatter plot

Correlation heatmap

Summary statistics

These visuals help highlight how key features relate to the diabetes outcome.

**Power BI Dashboard**

A Power BI dashboard was created to provide interactive insights:

Diabetes prevalence

Glucose trends by age group

BMI comparison between diabetic & non-diabetic patients

Outcome-based health indicator analysis

Patient summary table

This dashboard helps interpret the data in a simple and visually engaging way.

**Key Insights**

Higher glucose levels strongly correlate with diabetes

Patients with higher BMI and older age show greater risk

Roughly one-third of patients in the dataset are diabetic

Correlation heatmap highlights glucose and BMI as top predictors

**Tech Stack**

Python: Pandas, NumPy, Matplotlib, Seaborn

Power BI Desktop

ReportLab (PDF generation)

**Project Files**

diabetes.csv – Dataset

diabetes_analysis.py – Python analysis script

Healthcare Data Analysis – Diabetes Risk.pbix – Power BI dashboard

healthcare_diabetes_risk_analysis_results.pdf – Final report

**How to Run**

Install dependencies:

pip install -r requirements.txt


Run the analysis script:

python diabetes_analysis.py


View outputs in the outputs/ folder.

**Result PDF**

A full results report is included:
healthcare_diabetes_risk_analysis_results.pdf
