import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Specify the Excel file path
excel_file = 'test2.xls'

# Specify the sheet name in the Excel file
sheet_name = 'Loss'

# Specify the column names for X-axis and Y-axis
x_column = 'Year'
y_column = 'Value'

# Specify the range of rows you want to select (e.g., rows 2 to 10)
start_row = 0  # Adjust as needed
end_row = 8  # Adjust as needed

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract X and Y data from the selected range of rows
x_data = df.loc[start_row:end_row, x_column]
y_data = df.loc[start_row:end_row, y_column]

# Create a line chart
plt.plot(x_data, y_data, marker='o', linestyle='-')


# Add labels and a title
plt.xlabel(x_column)
plt.ylabel('Tons')
plt.title('Loss of Rice')

# Disable scientific notation on the Y-axis
plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

# Show the chart
plt.grid(True)
plt.show()
