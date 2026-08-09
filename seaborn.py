import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
# Update this path to where your file is stored:
df = pd.read_csv(r'C:\archive (1)\mpg_raw.csv')

print(df.head())
df.info()
print(df.shape)
print(df.describe())
print(df.describe(exclude='number'))
print(df.isnull().sum())



tips = sns.load_dataset("tips")

sns.set_style("whitegrid")

sns.histplot(
    data=tips,
    x="tip",
    hue="day",
    element="step"
)

plt.show()


sns.displot(
    data=tips,
    x="day",
    hue="sex",
    multiple="dodge",
    shrink=0.8,
    palette="Set1",
    hue_order=["Female", "Male"]
)

plt.show()


sns.set_style("darkgrid")
sns.set_context("notebook", font_scale=1.25)

sns.ecdfplot(
    data=tips,
    x="tip",
    hue="time",
    palette="summer",
    linewidth=3
)

plt.show()
