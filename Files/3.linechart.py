import lightningchart as lc
import pandas as pd
import numpy as np

# Load your LightningChart license key
with open('D:/fatemeh_ajam/lightningChart/A/license-key', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the dataset
file_path = 'dataset/WLD_RTFP_country_2024-11-04.csv'
data = pd.read_csv(file_path)

# Filter data for a specific country (example: Afghanistan)
country = 'Afghanistan'
country_data = data[data['country'] == country].dropna(subset=['Open', 'High', 'Low', 'Close'])

# Check if data is available
if country_data.empty:
    print("No data available for the specified indicators in this country.")
else:
    # Convert dates to datetime and extract year as timestamps (in milliseconds for LightningChart)
    dates = pd.to_datetime(country_data['date'])
    dates_numeric = dates.astype(np.int64) // 10**6  # Convert to milliseconds

    # Extract other values
    open_values = country_data['Open'].values
    high_values = country_data['High'].values
    low_values = country_data['Low'].values
    close_values = country_data['Close'].values

    # Initialize LightningChart with a theme
    chart = lc.ChartXY(
        theme=lc.Themes.Dark,
        title="Time Series Plot of Open, High, Low, and Close Prices"
    )

    # Set axis bounds to help display data correctly and format X-axis for dates
    x_axis = chart.get_default_x_axis()
    x_axis.set_interval(dates_numeric.min(), dates_numeric.max())
    x_axis.set_title('Year')
    x_axis.set_tick_strategy('DateTime', utc=True)  # Use DateTime format for X-axis to display years

    y_axis = chart.get_default_y_axis()
    y_axis.set_title('Value')

    # Add line series for each indicator with custom colors and labels
    open_series = chart.add_line_series().set_name('Open Value').set_line_color(lc.Color(128, 0, 128))  # Purple
    open_series.add(dates_numeric, open_values)

    high_series = chart.add_line_series().set_name('High Value').set_line_color(lc.Color(0, 0, 255))  # Blue
    high_series.add(dates_numeric, high_values)

    low_series = chart.add_line_series().set_name('Low Value').set_line_color(lc.Color(255, 255, 0))  # Yellow
    low_series.add(dates_numeric, low_values)

    close_series = chart.add_line_series().set_name('Close Value').set_line_color(lc.Color(255, 192, 203))  # Pink
    close_series.add(dates_numeric, close_values)

    # Add a legend to the chart and ensure it’s populated with each series
    legend = chart.add_legend()
    legend.add(open_series)
    legend.add(high_series)
    legend.add(low_series)
    legend.add(close_series)

    # Open the chart
    chart.open()
    