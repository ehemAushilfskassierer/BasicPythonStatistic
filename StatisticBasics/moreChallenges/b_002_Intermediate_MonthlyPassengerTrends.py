"""
b_002_Intermediate_MonthlyPassengerTrends

Monthly Passenger Trends
Load flights dataset and plot a line chart of passengers over time (year & month).
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

dfFlights = sns.load_dataset("flights")

print(dfFlights.head())

dfFlights["date"] = pd.to_datetime(dfFlights["year"].astype(str) + "-" + dfFlights["month"].astype(str) + "-01")

sns.lineplot(data=dfFlights, x="date", y="passengers")
plt.title("Monthly Passenger Trends")
plt.xlabel("Date")
plt.ylabel("Number of Passengers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()