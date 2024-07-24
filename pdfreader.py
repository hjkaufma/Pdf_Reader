import pandas as pd
import re
# Read in the Excel file
df = pd.read_excel('patient_summary_C.B_excel.xlsx', header=None)

# Create an empty list to store the results
results = []
# Define a regex pattern for the date format MM/DD/YYYY
date_pattern = r'\d{1,2}/\d{1,2}/\d{4}'
# Initialize a variable to store the last date added to the results list
last_date_added = None
# Loop through each row in the first column of the DataFrame
for value in df[0]:
    # Check if the value is a date in the format MM/DD/YYYY
    # Search for the date pattern in the cell
    match = re.search(date_pattern, str(value))
    # If a date is found, check if it meets the criteria for adding to the results list
    if match:
        date = match.group()
        
        # Check if the date is equal to 05/13/1964 or if it is the same as the last date added
        if date == '5/13/1964' or date == '05/13/1964' or date == last_date_added:
            continue
        
        # Add the date to the results list
        results.append(date)
        
        # Update the last date added variable
        last_date_added = date
        continue
   
    # Check if the value contains 'dilt' (case insensitive)
    #ingredient
    if 'amiodarone' in str(value).lower():
        results.append(str(value))
        # Update the last date added variable
        last_date_added = date
        continue

# Write the results to a text file
with open('output.txt', 'w') as f:
    f.write('\n'.join(results))