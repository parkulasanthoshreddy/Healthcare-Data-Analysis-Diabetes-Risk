import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


# PATHS (YOUR PROJECT LOCATION)

PROJECT_DIR = Path(r"C:\Users\Santhosh\OneDrive\Desktop\projects\Healthcare Data Analysis – Diabetes Risk")
DATA_FILE   = PROJECT_DIR / r"dataset\diabetes.csv"
OUT_DIR     = PROJECT_DIR / "outputs"
FIG_DIR     = OUT_DIR / "figures"

OUT_DIR.mkdir(exist_ok=True, parents=True)
FIG_DIR.mkdir(exist_ok=True, parents=True)


# LOAD DATA

print(" Loading dataset from:", DATA_FILE)
df = pd.read_csv(DATA_FILE)

print(" Data loaded. Shape:", df.shape)
print(df.head())


cols_to_fix = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

for col in cols_to_fix:
    df[col] = df[col].replace(0, np.nan)

df[cols_to_fix] = df[cols_to_fix].fillna(df[cols_to_fix].mean())


# HELPER: SAVE AND CLOSE PLOTS

def save_plot(name: str):
    """Save current matplotlib figure and close it."""
    filepath = FIG_DIR / name
    plt.savefig(filepath, bbox_inches="tight")
    plt.close()
    print(f" Saved figure: {filepath}")

sns.set(style="whitegrid")

# 1) Outcome Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(x="Outcome", data=df)
plt.title("Diabetes Outcome Count (0 = No, 1 = Yes)")
plt.xlabel("Outcome")
plt.ylabel("Count")
save_plot("outcome_count.png")


# 2) Age vs BMI Scatter (Colored by Outcome)

plt.figure(figsize=(6, 4))
sns.scatterplot(x="Age", y="BMI", hue="Outcome", data=df, alpha=0.7)
plt.title("Age vs BMI by Diabetes Outcome")
plt.xlabel("Age")
plt.ylabel("BMI")
save_plot("age_bmi.png")


# 3) Glucose Distribution

plt.figure(figsize=(6, 4))
sns.histplot(df["Glucose"], kde=True)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.ylabel("Frequency")
save_plot("glucose_dist.png")


# 4) Correlation Heatmap

plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
save_plot("correlation_heatmap.png")


# CALCULATE KEY INSIGHTS

total_records = len(df)
positive_cases = int(df["Outcome"].sum())
negative_cases = total_records - positive_cases
positive_rate = (positive_cases / total_records) * 100

avg_glucose = df["Glucose"].mean()
avg_bmi = df["BMI"].mean()
avg_age = df["Age"].mean()

insights = f"""
Healthcare Data Analysis – Diabetes Risk

Dataset Summary
• Total records: {total_records}
• Diabetes positive cases (Outcome=1): {positive_cases}
• Diabetes negative cases (Outcome=0): {negative_cases}
• Diabetes prevalence in this dataset: {positive_rate:.2f}%

Key Health Indicators (Averages)
• Average Glucose Level: {avg_glucose:.2f}
• Average BMI: {avg_bmi:.2f}
• Average Age: {avg_age:.2f} years

High-Level Insights
• Individuals with higher glucose levels are more likely to be diagnosed with diabetes.
• Higher BMI is also associated with increased diabetes risk.
• Age combined with BMI shows clear clustering of higher-risk groups.
• Correlation heatmap helps identify which features are most related to the Outcome.
"""

print(" Insights summary:")
print(insights)


# EXPORT PDF REPORT

pdf_path = OUT_DIR / "Diabetes_Risk_Analysis_Report.pdf"
styles = getSampleStyleSheet()
doc = SimpleDocTemplate(str(pdf_path), pagesize=A4)

story = []

# Title
story.append(Paragraph("<b>Healthcare Data Analysis – Diabetes Risk</b>", styles["Title"]))
story.append(Spacer(1, 12))

# Insights text (convert newlines to <br/> for PDF)
story.append(Paragraph(insights.replace("\n", "<br/>"), styles["Normal"]))
story.append(Spacer(1, 12))

# Add images to the PDF in order
figures = [
    "outcome_count.png",
    "age_bmi.png",
    "glucose_dist.png",
    "correlation_heatmap.png",
]

for fig_name in figures:
    img_path = FIG_DIR / fig_name
    if img_path.exists():
        story.append(Image(str(img_path), width=400, height=300))
        story.append(Spacer(1, 24))
    else:
        print(f" Figure not found, skipping in PDF: {img_path}")

doc.build(story)

print(" Analysis complete.")
print(" PDF report saved at:", pdf_path)
