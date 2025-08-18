"""
c_003_UpperIntermediate_LineChartOfDailyTemperatures

ine Chart of Daily Temperatures
Plot a line chart for 7 days of temperatures: [20, 21, 19, 22, 23, 20, 18].
"""
import matplotlib.pyplot as plt

lstTemps = [20, 21, 19, 22, 23, 20, 18]
lstDays = ["Monday", "Tuesday", "Wednesdays", "Thursday", "Friday", "Saturday", "Sunday"]

plt.figure(figsize=(8, 4))
plt.plot(lstDays, lstTemps, marker='o', linestyle='-', color='teal')
plt.title("c_003_UpperIntermediate_LineChartOfDailyTemperatures")
plt.grid()
plt.show()