import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_Sales_Dataset.xlsx")

male_sales = df[df["Gender"]=="Male"]["Total_Sales"]
female_sales = df[df["Gender"]=="Female"]["Total_Sales"]

t_stat,p_value = ttest_ind(male_sales,female_sales)

print("Hypothesis Testing")
print("---------------------")
print("T Statistic :",t_stat)
print("P Value :",p_value)

if p_value<0.05:
    print("Result : Significant Difference Exists")
else:
    print("Result : No Significant Difference")

sales=df.groupby("Gender")["Total_Sales"].mean()

plt.figure(figsize=(6,5))
sales.plot(kind="bar")
plt.title("Average Sales by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.savefig("hypothesis_chart.png")
plt.show()

summary=pd.DataFrame({
"Gender":["Male","Female"],
"Average Sales":[male_sales.mean(),female_sales.mean()]
})

summary.to_excel("hypothesis_summary.xlsx",index=False)

print("Task 4 Completed Successfully")