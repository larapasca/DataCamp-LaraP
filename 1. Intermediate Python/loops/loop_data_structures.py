# ITERATING ON DICTIONARIES
""" europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
for key,value in europe.items():
    print('the capital of',key,'is',value) """
    
# ITERATING ON NUMPY ARRAY
""" import numpy as np
# For loop over np_height
for height in np_height:
    print(height,'inches')

# For loop over np_baseball #Contiene un array 2d de (heights,weights)
for x in np.nditer(np_baseball) :
    print(x) """
    
# LOOPING PANDAS DF
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows() :
    print(lab) #label
    print(row) #row info
    
for lab, row in cars.iterrows() :
    print(lab + ':', row['cars_per_cap'])
    
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = cars.loc[lab, 'country'].upper()
    
# Use .apply(str.upper) instead of iteration
cars["COUNTRY"] = cars["country"].apply(str.upper)