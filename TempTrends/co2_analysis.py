import matplotlib.pyplot as plt
import pandas as pd
import math

# Load in the data with read_csv()
co2_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row
print(co2_data)
# clean data
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

# plot data
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('Average co2 Levels')
plt.xlabel('Years')
plt.title('CO2 level in ppm')
plt.show()  