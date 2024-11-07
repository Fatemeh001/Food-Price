# import lightningchart as lc
# import pandas as pd
# import numpy as np
# from datetime import datetime

# # Load license key
# with open('D:/fatemeh_ajam/lightningChart/A/license-key', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Load data
# data = pd.read_csv('dataset/WLD_RTFP_country_2024-11-04.csv')

# # Filter data for a specific country (example: Afghanistan)
# country = 'Afghanistan'
# country_data = data[data['country'] == country].dropna(subset=['Open', 'High', 'Low', 'Close', 'Inflation'])

# # Check if data is available
# if country_data.empty:
#     print("No data available for the specified indicators in this country.")
# else:
#     # Convert date column to numeric values for plotting
#     dates = pd.to_datetime(country_data['date']).map(datetime.toordinal)
#     open_values = country_data['Open'].values
#     high_values = country_data['High'].values
#     low_values = country_data['Low'].values
#     close_values = country_data['Close'].values
#     inflation_values = country_data['Inflation'].values

#     # Initialize LightningChart with Black theme
#     chart = lc.ChartXY(
#         theme=lc.Themes.Black,
#         title=f"Economic Indicators for {country}"
#     )

#     # Add legend to the chart
#     legend = chart.add_legend()

#     # List of indicators to plot
#     indicators = {
#         'Open': open_values,
#         'High': high_values,
#         'Low': low_values,
#         'Close': close_values,
#         'Inflation': inflation_values
#     }

#     # Add line series for each indicator and set the name in the legend
#     for name, y_values in indicators.items():
#         line_series = chart.add_line_series().set_name(name)  # Set name for each series
#         line_series.add(dates, y_values)
#         legend.add(line_series)  # Attach each series to the legend

#     # Open the chart with the legend
#     chart.open()

import lightningchart as lc
from lightningchart import Color
import pandas as pd

# Load your license key
with open('D:/fatemeh_ajam/lightningChart/A/license-key', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load data
data = pd.read_csv('dataset/WLD_RTFP_country_2024-11-04.csv')

# Filter data for a specific country (example: Afghanistan)
country = 'Afghanistan'
country_data = data[data['country'] == country].dropna(subset=['Open', 'High', 'Low', 'Close', 'Inflation'])

# Check if data is available
if country_data.empty:
    print("No data available for the specified indicators in this country.")
else:
    # Extract time series values
    dates = pd.to_datetime(country_data['date']).dt.strftime('%Y-%m-%d')
    open_values = country_data['Open'].values
    high_values = country_data['High'].values
    low_values = country_data['Low'].values
    close_values = country_data['Close'].values
    inflation_values = country_data['Inflation'].values

    # Initialize LightningChart with Black theme
    chart = lc.ChartXY(
        theme=lc.Themes.Black,
        title=f"Economic Indicators for {country}"
    )

    # Add legend to the chart
    legend = chart.add_legend()

    # List of indicators to plot with their respective colors
    indicators = {
        'Open': (open_values, Color('#FF0000')),  # Red
        'High': (high_values, Color('#00FF00')),  # Green
        'Low': (low_values, Color('#0000FF')),    # Blue
        'Close': (close_values, Color('#000000')) # Black
    }

    # Add line series for each indicator and set the name and color
    for name, (y_values, color) in indicators.items():
        line_series = chart.add_line_series().set_name(name).set_line_color(color)
        line_series.add(dates, y_values)
        legend.add(line_series)  # Attach each series to the legend

    # Open the chart with the legend
    chart.open()
