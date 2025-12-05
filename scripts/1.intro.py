# Bitcoin Price Analysis


# Libraries and Data
# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Load the data
df = pd.read_csv("C:/TSF.2.bitcoin_price.csv")
df.head()

# Time Series Index
# Convert 'Date' to a Datetime and set as index
df['Date'] = pd.to_datetime(df['Date'], format = "%Y-%m-%d")
df.set_index('Date', inplace=True)
df.head()

# Select the Bitcoin Data for November 2021
df.loc['2021-11-09']

# Resampling to Monthly Frequency and calculate the mean closing price
df.resample('M').mean()

# Exploring Data
# 7-Day rolling average of the closing price 
df['7_day_roll'] = df['Close'].rolling(window=7).mean()
df[['Close', '7_day_roll']].loc['2023'].plot()
plt.show()

# Find out the highest average month
df.resample('M').mean()['Close'].idxmax()

# Calculate Daily Returns
df['daily_returns'] = df['Close'].pct_change()*100

# Days with more than 10% change in closing price
df[abs(df['daily_returns']) > 10]

