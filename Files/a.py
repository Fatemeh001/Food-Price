import pandas as pd
import lightningchart as lc
import numpy as np



with open('D:/fatemeh_ajam/lightningChart/A/license-key', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

file_path = 'dataset/WLD_RTFP_country_2024-11-04.csv'  
df = pd.read_csv(file_path)



# df['date'] = pd.to_datetime(df['date'])

# missing_data = df.isnull().sum()  


# for column in ['Open', 'High', 'Low', 'Close']: 
#     df[column] = df.groupby('country')[column].transform(lambda x: x.fillna(method='ffill').fillna(method='bfill'))

# missing_data_after_fill = df.isnull().sum()

# country = 'Afghanistan'
# current_year = df['date'].dt.year.max() 
# three_years_ago = current_year - 3 
# df_afghanistan_last_three_years = df[(df['country'] == country) & (df['date'].dt.year >= three_years_ago)]  

# chart = lc.ChartXY(theme=lc.Themes.White)

# for i in range(len(df_afghanistan_last_three_years)):
#     open_price = df_afghanistan_last_three_years['Open'].iloc[i]
#     close_price = df_afghanistan_last_three_years['Close'].iloc[i]
#     high_price = df_afghanistan_last_three_years['High'].iloc[i]
#     low_price = df_afghanistan_last_three_years['Low'].iloc[i]
#     date = int(df_afghanistan_last_three_years['date'].iloc[i].timestamp() * 1000) 

#     color = lc.Color(0, 150, 0, 255) if close_price >= open_price else lc.Color(150, 0, 0, 255)

#     chart.add_line_series().add([date, high_price], [date, low_price], color='black', lineWidth=1)

#     rect = chart.add_rectangle_series().add(
#         x1=date, y1=open_price, 
#         x2=date + 86400000, y2=close_price  
#     )
#     rect.set_color(color)  

# x_axis = chart.get_default_x_axis()
# x_axis.set_interval(int(df_afghanistan_last_three_years['date'].min().timestamp() * 1000), int(df_afghanistan_last_three_years['date'].max().timestamp() * 1000))  # Set X axis range
# x_axis.set_title('Date')
# x_axis.set_tick_strategy('DateTime', utc=True) 

# chart.set_title('Candlestick Chart for Afghanistan Last Three Years Data')
# chart.get_default_y_axis().set_title('Price')

# chart.open()



# Ensure the date is correctly formatted
df['date'] = pd.to_datetime(df['date'])

# Check for missing values
missing_data = df.isnull().sum()  # Count missing values in each column


# Fill missing values for each column based on the same column values and country
for column in ['Open', 'High', 'Low', 'Close']:  # Specify the columns to fill
    df[column] = df.groupby('country')[column].transform(lambda x: x.fillna(method='ffill').fillna(method='bfill'))

# Verify that there are no missing values after filling
missing_data_after_fill = df.isnull().sum()


# Filter data for Afghanistan
country = 'Afghanistan'
current_year = df['date'].dt.year.max() 
three_years_ago = current_year - 3 
df_afghanistan_last_three_years = df[(df['country'] == country) & (df['date'].dt.year >= three_years_ago)]  

# Create candlestick chart
chart = lc.ChartXY(theme=lc.Themes.Light)

# Draw candlesticks
for i in range(len(df_afghanistan_last_three_years)):
    open_price = df_afghanistan_last_three_years['Open'].iloc[i]
    close_price = df_afghanistan_last_three_years['Close'].iloc[i]
    high_price = df_afghanistan_last_three_years['High'].iloc[i]
    low_price = df_afghanistan_last_three_years['Low'].iloc[i]
    date = int(df_afghanistan_last_three_years['date'].iloc[i].timestamp() * 1000)  # Convert to timestamp in milliseconds

    # Determine rectangle color (brighter shades for better visibility)
    color = lc.Color(0, 200, 0, 255) if close_price >= open_price else lc.Color(200, 0, 0, 255)

    # Draw high-low lines with increased thickness
    chart.add_line_series().add([date, high_price], [date, low_price], color='black', lineWidth=2)

    # Draw rectangle for open and close prices
    rect = chart.add_rectangle_series().add(
        x1=date, y1=open_price, 
        x2=date + 86400000, y2=close_price  # Add 86400000 milliseconds for one day
    )
    rect.set_color(color)  # Set rectangle color

# Add moving average
moving_average = df_afghanistan_last_three_years['Close'].rolling(window=20).mean()  # 20-day moving average
for i in range(len(moving_average)):
    if not np.isnan(moving_average.iloc[i]):
        date = int(df_afghanistan_last_three_years['date'].iloc[i].timestamp() * 1000)
        chart.add_line_series().add([date, moving_average.iloc[i]], [date, moving_average.iloc[i]], color='blue', lineWidth=1)

# Set date for X axis
x_axis = chart.get_default_x_axis()
x_axis.set_interval(int(df_afghanistan_last_three_years['date'].min().timestamp() * 1000), int(df_afghanistan_last_three_years['date'].max().timestamp() * 1000))  # Set X axis range
x_axis.set_title('Date')
x_axis.set_tick_strategy('DateTime', utc=True)  # Use DateTime format for X axis


# Set title and axes
chart.set_title('Candlestick Chart for Afghanistan Last Three Years Data')
chart.get_default_y_axis().set_title('Price')

# Enable grid lines
y_axis = chart.get_default_y_axis()

# Display the chart
chart.open()
