# import lightningchart as lc
# import pandas as pd
# import numpy as np

# # Load the dataset
# file_path = 'dataset/WLD_RTFP_country_2024-11-04.csv'
# data = pd.read_csv(file_path)

# # Load your LightningChart license key
# with open('D:/fatemeh_ajam/lightningChart/A/license-key', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Calculate the correlation matrix for selected indicators
# numeric_data = data[['Open', 'High', 'Low', 'Close', 'Inflation']]
# corr_matrix = numeric_data.corr()
# corr_array = corr_matrix.to_numpy()
# labels = corr_matrix.columns  # Extract column labels for custom ticks

# # Create the chart
# chart = lc.ChartXY(
#     title="Economic Indicators Correlation Heatmap",
#     theme=lc.Themes.Dark
# )

# # Get the grid size based on the correlation matrix shape
# grid_size_x, grid_size_y = corr_array.shape

# # Create the heatmap grid series
# heatmap_series = chart.add_heatmap_grid_series(
#     columns=grid_size_x,
#     rows=grid_size_y,
# )

# # Set heatmap position and grid settings
# heatmap_series.set_start(x=0, y=0)
# heatmap_series.set_end(x=grid_size_x, y=grid_size_y)
# heatmap_series.set_step(x=1, y=1)

# # Apply intensity values from the correlation matrix
# heatmap_series.invalidate_intensity_values(corr_array.tolist())
# heatmap_series.set_intensity_interpolation(False)

# # Define the color palette for correlation values
# palette_steps = [
#     {"value": 1, "color": lc.Color('blue')},  # Strong negative correlation
#     {"value": 0, "color": lc.Color('white')},  # No correlation
#     {"value": -1, "color": lc.Color('red')}     # Strong positive correlation
# ]

# # Set the color palette to the heatmap
# heatmap_series.set_palette_colors(
#     steps=palette_steps,
#     look_up_property='value',
#     interpolate=True
# )

# # Customize the x-axis and y-axis with indicator labels
# x_axis = chart.get_default_x_axis()
# y_axis = chart.get_default_y_axis()

# x_axis.set_tick_strategy('Empty')
# y_axis.set_tick_strategy('Empty')

# # Add custom ticks for each indicator
# for i, label in enumerate(labels):
#     custom_tick_x = x_axis.add_custom_tick()
#     custom_tick_x.set_value(i + 0.5)
#     custom_tick_x.set_text(label)

#     custom_tick_y = y_axis.add_custom_tick()
#     custom_tick_y.set_value(i + 0.5)
#     custom_tick_y.set_text(label)

# # Add a legend for correlation values
# chart.add_legend(data=heatmap_series).set_margin(-20)

# # Open the chart
# chart.open()
import lightningchart as lc

# Print the version of LightningChart
import lightningchart as lc

# بررسی ورژن با استفاده از توابع موجود در ماژول
print(lc.get_version())

