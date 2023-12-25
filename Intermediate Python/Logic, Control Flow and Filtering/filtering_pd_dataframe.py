""" 
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd

my_dict = {"country":names,"drives_right":dr,"cars_per_cap":cpc}
cars = pd.DataFrame(my_dict)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)  

#Select countries with more than 500 cars_per_cap
'''
1. Select the column (cars_per_cap)
2. Do comparison on that column and store its result
3. Use result to select countries'''
drives_much = cars['cars_per_cap'] > 500
print(cars[drives_much]) 
"""

""" # Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
cars['drives_right']

# Use dr to subset cars: sel
sel = cars['drives_right']

# Print sel
print(cars[sel == True])

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel) """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)