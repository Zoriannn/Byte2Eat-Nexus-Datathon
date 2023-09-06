import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Specify the Excel file path
excel_file = 'test2.xls'

# Specify the sheet name in the Excel file
sheet_name = 'Production'

# Specify the column names for X-axis and Y-axis
x_column = 'Year'
y_column = 'Value'

# Specify the range of rows you want to select (e.g., rows 2 to 10)
start_row = 9  # Adjust as needed
end_row = 17  # Adjust as needed

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract X and Y data from the selected range of rows
x_data = df.loc[start_row:end_row, x_column]
y_data = df.loc[start_row:end_row, y_column]

# Create a line chart
plt.plot(x_data, y_data, marker='o', linestyle='-')


# Calculate the interquartile range (IQR) for the 'Value' column
Q1 = y_data.quantile(0.25)
Q3 = y_data.quantile(0.75)
IQR = Q3 - Q1

# Define a threshold for outliers (e.g., 1.5 times the IQR)
outlier_threshold = 1.5 * IQR

# Detect outliers
outliers = y_data[(y_data < (Q1 - outlier_threshold)) | (y_data > (Q3 + outlier_threshold))]

# Print the outliers
print("Outliers:")
print(outliers)


# Add labels and a title
plt.xlabel(x_column)
plt.ylabel('Tons')
plt.title('Rice Production')

# Disable scientific notation on the Y-axis
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

# Show the chart
plt.grid(True)
plt.show()
