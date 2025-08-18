"""
d_005_Challenging_MiniDataDashboard

Mini Data Dashboard
Load a CSV file of your choice (e.g., sales data) and create three plots:
Sales over time (line)
Top 5 products (bar)
Category distribution (pie)
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dfData = pd.read_csv("sales_data.csv")
print(dfData.head())

sales_over_time = dfData.groupby("Date")["Sales"].sum()
top_products = dfData.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
category_counts = dfData["Category"].value_counts()

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("d_005_Challenging_MiniDataDashboard", fontsize=14)

axes[0].plot(sales_over_time.index, sales_over_time.values, marker="o", linestyle="dashed", label="Sales")
axes[0].set_title("Sales Over Time")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Sales")
axes[0].grid(True)
axes[0].legend()
axes[0].xaxis.set_major_locator(mdates.AutoDateLocator(minticks=5, maxticks=8))
axes[0].tick_params(axis="x", rotation=45)

axes[1].bar(top_products.index, top_products.values, color="skyblue")
axes[1].set_title("Top 5 Products by Sales")
axes[1].set_ylabel("Total Sales")
axes[1].tick_params(axis="x", rotation=45)

axes[2].pie(category_counts.values, labels=category_counts.index, autopct="%1.1f%%", startangle=90)
axes[2].set_title("Category Distribution")

plt.tight_layout()
plt.show()